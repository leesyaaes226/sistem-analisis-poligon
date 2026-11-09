import streamlit as st
import math

# ==================================================
# 1. TETAPAN APLIKASI
# ==================================================

st.set_page_config(
    page_title="Sistem Pengiraan Poligon Sekata",
    page_icon="📐",
    layout="wide"
)

# ==================================================
# 2. SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "hasil_sisi" not in st.session_state:
    st.session_state.hasil_sisi = None


# ==================================================
# 3. DATA NAMA POLIGON
# ==================================================

nama_poligon = {
    3: "Segi Tiga Sama Sisi",
    4: "Segi Empat Sama",
    5: "Pentagon",
    6: "Heksagon",
    7: "Heptagon",
    8: "Oktagon",
    9: "Nonagon",
    10: "Dekagon",
    11: "Hendekagon",
    12: "Dodekagon"
}


def dapatkan_nama(sisi):

    if sisi in nama_poligon:
        return nama_poligon[sisi]

    return f"Poligon {sisi} Sisi"


# ==================================================
# 4. FUNGSI MELUKIS POLIGON
# ==================================================

def lukis_poligon(sisi):

    titik = []

    for i in range(sisi):

        sudut = (
            2 * math.pi * i / sisi
            - math.pi / 2
        )

        x = 150 + 110 * math.cos(sudut)
        y = 150 + 110 * math.sin(sudut)

        titik.append(f"{x:.2f},{y:.2f}")

    koordinat = " ".join(titik)

    svg = f"""
    <svg width="100%" height="320"
         viewBox="0 0 300 300"
         xmlns="http://www.w3.org/2000/svg">

        <polygon
            points="{koordinat}"
            fill="#B9D9F5"
            stroke="#16365C"
            stroke-width="4"
            stroke-linejoin="round"
        />

    </svg>
    """

    st.markdown(
        svg,
        unsafe_allow_html=True
    )


# ==================================================
# 5. FUNGSI PENGIRAAN
# ==================================================

def kira_poligon(sisi):

    jumlah = (sisi - 2) * 180

    setiap = jumlah / sisi

    return jumlah, setiap


def format_sudut(nilai):

    if nilai.is_integer():
        return f"{nilai:.0f}°"

    return f"{nilai:.2f}°"


# ==================================================
# 6. HOME PAGE
# ==================================================

if st.session_state.page == "Home":

    st.title("SISTEM PENGIRAAN POLIGON SEKATA")

    st.subheader(
        "Regular Polygon Calculator"
    )

    st.write(
        "Selamat datang ke Sistem Pengiraan Poligon Sekata. "
        "Sistem ini dibangunkan untuk membantu pengguna "
        "mengira jumlah sudut pedalaman dan setiap sudut "
        "bagi sesuatu poligon sekata."
    )

    st.divider()

    st.markdown("## PENGENALAN SISTEM")

    st.write(
        "Melalui sistem ini, pengguna hanya perlu "
        "memasukkan bilangan sisi poligon. Sistem akan "
        "mengenal pasti bentuk poligon dan memaparkan "
        "gambar, nama, formula serta langkah pengiraan "
        "secara automatik."
    )

    st.divider()

    st.markdown("## FUNGSI UTAMA")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            "**PENGENALAN POLIGON**\n\n"
            "Mengenal pasti nama dan bentuk poligon."
        )

    with col2:

        st.info(
            "**PENGIRAAN SUDUT**\n\n"
            "Mengira jumlah dan setiap sudut pedalaman."
        )

    with col3:

        st.info(
            "**LANGKAH PENGIRAAN**\n\n"
            "Memaparkan formula dan cara pengiraan."
        )

    st.divider()

    st.markdown("## FORMULA MATEMATIK")

    col1, col2 = st.columns(2)

    with col1:

        st.latex(
            r"S=(n-2)\times180^\circ"
        )

        st.caption(
            "Formula jumlah sudut pedalaman"
        )

    with col2:

        st.latex(
            r"A=\frac{(n-2)\times180^\circ}{n}"
        )

        st.caption(
            "Formula setiap sudut pedalaman"
        )

    st.divider()

    st.markdown("## MULAKAN PENGIRAAN")

    st.write(
        "Tekan butang di bawah untuk mula menganalisis "
        "bentuk poligon."
    )

    if st.button(
        "MULA PENGIRAAN",
        type="primary",
        use_container_width=True
    ):

        st.session_state.page = "Pengiraan"

        st.rerun()

    st.divider()

    st.caption(
        "Projek ASK Tingkatan 2 | 2026"
    )


# ==================================================
# 7. CALCULATION PAGE
# ==================================================

elif st.session_state.page == "Pengiraan":

    st.title("PENGIRAAN POLIGON SEKATA")

    st.write(
        "Masukkan bilangan sisi poligon untuk mendapatkan "
        "analisis dan pengiraan secara automatik."
    )

    st.divider()

    # INPUT PENGGUNA

    with st.container(border=True):

        st.markdown("### INPUT BILANGAN SISI")

        with st.form("borang_pengiraan"):

            sisi_input = st.number_input(
                "Masukkan bilangan sisi:",
                min_value=3,
                max_value=1000,
                value=6,
                step=1
            )

            kira = st.form_submit_button(
                "ANALISIS POLIGON",
                type="primary",
                use_container_width=True
            )

        if kira:

            st.session_state.hasil_sisi = int(sisi_input)

    # PAPARAN KEPUTUSAN

    if st.session_state.hasil_sisi is not None:

        sisi = st.session_state.hasil_sisi

        nama = dapatkan_nama(sisi)

        jumlah, setiap = kira_poligon(sisi)

        st.divider()

        st.success(
            "Analisis poligon berjaya!"
        )

        # NAMA DAN GAMBAR

        st.markdown("## HASIL ANALISIS POLIGON")

        st.subheader(nama.upper())

        col1, col2 = st.columns(2)

        with col1:

            lukis_poligon(sisi)

        with col2:

            st.markdown("### MAKLUMAT POLIGON")

            st.metric(
                "Bilangan sisi",
                sisi
            )

            st.metric(
                "Jumlah sudut pedalaman",
                format_sudut(float(jumlah))
            )

            st.metric(
                "Setiap sudut pedalaman",
                format_sudut(setiap)
            )

        st.divider()

        # PENGIRAAN JUMLAH SUDUT

        st.markdown(
            "## 1. JUMLAH SUDUT PEDALAMAN"
        )

        st.write(
            "Formula yang digunakan:"
        )

        st.latex(
            r"S=(n-2)\times180^\circ"
        )

        st.markdown("**Langkah pengiraan:**")

        st.write(
            f"1. Gantikan nilai n dengan {sisi}."
        )

        st.latex(
            rf"S=({sisi}-2)\times180^\circ"
        )

        st.write(
            f"2. Tolak bilangan sisi dengan 2."
        )

        st.latex(
            rf"S={sisi-2}\times180^\circ"
        )

        st.write(
            "3. Darabkan hasil dengan 180°."
        )

        st.latex(
            rf"S={jumlah}^\circ"
        )

        st.success(
            f"Jumlah sudut pedalaman = {jumlah}°"
        )

        st.divider()

        # PENGIRAAN SETIAP SUDUT

        st.markdown(
            "## 2. SETIAP SUDUT PEDALAMAN"
        )

        st.write(
            "Formula yang digunakan:"
        )

        st.latex(
            r"A=\frac{S}{n}"
        )

        st.markdown("**Langkah pengiraan:**")

        st.write(
            f"1. Bahagikan jumlah sudut dengan "
            f"bilangan sisi, iaitu {sisi}."
        )

        st.latex(
            rf"A=\frac{{{jumlah}^\circ}}{{{sisi}}}"
        )

        st.write(
            "2. Dapatkan nilai setiap sudut pedalaman."
        )

        st.latex(
            rf"A={format_sudut(setiap)}"
        )

        st.success(
            f"Setiap sudut pedalaman = "
            f"{format_sudut(setiap)}"
        )

        st.divider()

        # RUMUSAN

        st.markdown("## RUMUSAN KEPUTUSAN")

        with st.container(border=True):

            st.subheader(nama)

            st.write(
                f"Bilangan sisi: {sisi}"
            )

            st.write(
                f"Jumlah sudut pedalaman: {jumlah}°"
            )

            st.write(
                f"Setiap sudut pedalaman: "
                f"{format_sudut(setiap)}"
            )

        st.caption(
            "Nota: Pengiraan setiap sudut adalah berdasarkan "
            "andaian bahawa poligon tersebut ialah poligon sekata."
        )

    st.divider()

    # BUTANG KEMBALI

    if st.button(
        "KEMBALI KE HOME",
        use_container_width=True
    ):

        st.session_state.page = "Home"

        st.rerun()

    st.caption(
        "Sistem Pengiraan Poligon Sekata | Projek ASK 2026"
    )
