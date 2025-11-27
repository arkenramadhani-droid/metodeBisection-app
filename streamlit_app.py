import streamlit as st
import numpy as np

def bisection_method(func_str, a, b, tol, max_iter):
    """
    Menghitung akar fungsi non-linier menggunakan Metode Biseksi.
    :param func_str: String yang merepresentasikan fungsi f(x).
    :param a: Batas bawah interval.
    :param b: Batas atas interval.
    :param tol: Toleransi (error/akurasi).
    :param max_iter: Jumlah iterasi maksimum.
    :return: Tuple (akar, tabel_iterasi, status)
    """
    
    try:
        f = lambda x: eval(func_str)
    except NameError:
        return None, [], "Gagal: Terdapat kesalahan sintaks pada fungsi $f(x)$."
    except Exception as e:
        return None, [], f"Gagal saat mengevaluasi fungsi: {e}"

    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        return None, [], "Gagal: $f(a)$ dan $f(b)$ harus berlawanan tanda ($f(a) \cdot f(b) < 0$). Coba interval lain."

    iter_count = 0
    c = a # Inisialisasi
    table_data = []

    while (b - a) >= tol and iter_count < max_iter:
        
        c = (a + b) / 2
        fc = f(c)
        
        table_data.append({
            "Iterasi": iter_count + 1,
            "a": f"{a:.6f}",
            "b": f"{b:.6f}",
            "c": f"{c:.6f}",
            "f(c)": f"{fc:.6f}",
            "Error (b-a)": f"{abs(b-a):.6f}",
        })
        
        if fc == 0:
            break 
        elif fa * fc < 0:
            b = c 
        else:
            a = c 
        
        iter_count += 1

    # Tentukan status akhir
    if abs(b - a) < tol:
        status = f"✅ Akar berhasil ditemukan pada iterasi ke-{iter_count} dengan error kurang dari {tol}."
    else:
        status = f"⚠️ Perhitungan berhenti setelah {max_iter} iterasi, toleransi belum tercapai."

    return c, table_data, status

st.set_page_config(
    page_title="Solusi SPNL: Metode Biseksi",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Solusi SPNL dengan Metode Biseksi")
st.markdown("Aplikasi web sederhana untuk mencari akar fungsi non-linier $f(x)$ menggunakan Metode Biseksi.")

col1, col2, col3 = st.columns(3)

with col1:
    # Menggunakan 'st.text_input' untuk fungsi (string)
    func_str = st.text_input(
        "Fungsi $f(x)$:",
        value="x**3 - 7*x**2 + 14*x - 6",
        help="Contoh: x**2 - 4 atau np.exp(-x) - x"
    )

with col2:
    a = st.number_input("Batas Bawah Interval ($a$):", value=0.0, step=0.1)

with col3:
    b = st.number_input("Batas Atas Interval ($b$):", value=1.0, step=0.1)

col4, col5 = st.columns(2)

with col4:
    tol = st.number_input("Toleransi ($\epsilon$):", value=0.0001, format="%.6f", help="Akurasi yang diinginkan.")

with col5:
    max_iter = st.number_input("Maksimum Iterasi:", value=100, step=1)

if st.button("🚀 Hitung Akar", type="primary"):
    akar, tabel, status = bisection_method(func_str, a, b, tol, max_iter)

    st.subheader("📝 Hasil Perhitungan")
    st.info(status)

    if akar is not None:
        try:
            f = lambda x: eval(func_str)
            f_akar = f(akar)
        except Exception:
            # Handle jika fungsi gagal dievaluasi di sini (meskipun seharusnya sudah terdeteksi di fungsi bisection)
            f_akar = float('nan') 

        st.metric(
            label="Nilai Akar ($c$)", 
            value=f"{akar:.6f}",
            # 2. Ganti delta untuk menampilkan f(c) yang dihitung langsung
            delta=f"f(c) = {f_akar:.6e}" 
        )

        st.subheader("📚 Detail Iterasi")
        st.dataframe(tabel, use_container_width=True)

    st.markdown("---")
    st.caption("Catatan: Fungsi matematika seperti cos, sin, exp, log harus diawali dengan 'np.' karena menggunakan library NumPy.")

st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">',
    unsafe_allow_html=True
)
ig_color = "linear-gradient(45deg, #f09433 0%,#e6684e 25%,#c63683 50%,#8b33a5 75%,#515bd4 100%)"
st.markdown(
    f"""
    <a href="https://www.instagram.com/aryakndrn/" target="_blank" style="text-decoration: none;">
        <div style="
            background: {ig_color};
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            text-align: center;
            display: inline-block;
            font-size: 16px;
            font-weight: bold;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);">
            <i class="fab fa-instagram"></i> Ikuti Arya Kendrian
        </div>
    </a>
    """,
    unsafe_allow_html=True
)
