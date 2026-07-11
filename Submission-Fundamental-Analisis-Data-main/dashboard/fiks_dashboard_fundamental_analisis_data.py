import os
import warnings

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import streamlit as st

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #F7FBF8 0%, #F3F7F4 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2.2rem;
        padding-right: 2.2rem;
        max-width: 1280px;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .custom-card {
        background: #FFFFFF;
        border: 1px solid #E3EEE7;
        border-radius: 18px;
        padding: 1.2rem 1.2rem 1rem 1.2rem;
        box-shadow: 0 6px 20px rgba(24, 61, 44, 0.06);
        margin-bottom: 1rem;
    }

    .hero-box {
        background: linear-gradient(135deg, #2D6A4F 0%, #40916C 100%);
        padding: 1.6rem 1.6rem 1.3rem 1.6rem;
        border-radius: 22px;
        color: white;
        box-shadow: 0 10px 28px rgba(45, 106, 79, 0.25);
        margin-bottom: 1.2rem;
    }

    .hero-title {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
        line-height: 1.2;
    }

    .hero-subtitle {
        font-size: 1rem;
        opacity: 0.95;
        margin-bottom: 0.55rem;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.16);
        border: 1px solid rgba(255,255,255,0.22);
        border-radius: 999px;
        padding: 0.35rem 0.8rem;
        font-size: 0.86rem;
        margin-right: 0.45rem;
        margin-top: 0.35rem;
    }

    .metric-box {
        background: #FFFFFF;
        border: 1px solid #E3EEE7;
        border-radius: 18px;
        padding: 1rem 1rem 0.9rem 1rem;
        box-shadow: 0 4px 16px rgba(20, 50, 30, 0.05);
    }

    .metric-label {
        color: #5E7467;
        font-size: 0.92rem;
        margin-bottom: 0.2rem;
    }

    .metric-value {
        color: #1B4332;
        font-size: 2rem;
        font-weight: 800;
        line-height: 1.1;
    }

    .metric-note {
        color: #7C8F84;
        font-size: 0.8rem;
        margin-top: 0.35rem;
    }

    .section-note {
        color: #5C6F65;
        font-size: 0.95rem;
        margin-top: -0.15rem;
        margin-bottom: 0.9rem;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #F8FCF9 0%, #EEF6F0 100%);
        border-right: 1px solid #E3EEE7;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }

    button[data-baseweb="tab"] {
        border-radius: 12px;
        padding: 0.55rem 1rem;
        background: #EDF5EF;
        border: 1px solid #E0EBE3;
        margin-right: 0.35rem;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background: #2D6A4F !important;
        color: white !important;
        border: 1px solid #2D6A4F !important;
    }

    .table-card {
        background: #FFFFFF;
        border: 1px solid #E3EEE7;
        border-radius: 16px;
        padding: 0.8rem;
        box-shadow: 0 4px 14px rgba(20, 50, 30, 0.05);
        margin-bottom: 1rem;
    }

    .soft-divider {
        height: 1px;
        background: linear-gradient(to right, rgba(0,0,0,0), #DCE9E0, rgba(0,0,0,0));
        margin-top: 0.8rem;
        margin-bottom: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

COLOR_PRIMARY = "#2D6A4F"
COLOR_GOLD = "#E9C46A"
COLOR_MUTED = "#B7E4C7"
COLOR_BG = "#F8FBF9"


@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "main_data.csv")
    df = pd.read_csv(csv_path)

    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df["revenue"] = df["price"] + df["freight_value"]

    return df


all_df = load_data()

# Filter default sesuai revisi notebook: periode 2017–2018
default_min_date = max(all_df["order_purchase_timestamp"].min().date(), pd.to_datetime("2017-01-01").date())
default_max_date = min(all_df["order_purchase_timestamp"].max().date(), pd.to_datetime("2018-12-31").date())

with st.sidebar:
    st.markdown("## E-Commerce")
    st.caption("Filter dashboard interaktif")
    st.markdown("---")

    date_range = st.date_input(
        "Filter Rentang Tanggal",
        value=[default_min_date, default_max_date],
        min_value=all_df["order_purchase_timestamp"].min().date(),
        max_value=all_df["order_purchase_timestamp"].max().date()
    )

    st.markdown("---")

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = all_df[
        (all_df["order_purchase_timestamp"].dt.date >= start_date) &
        (all_df["order_purchase_timestamp"].dt.date <= end_date)
    ].copy()
else:
    filtered_df = all_df[
        (all_df["order_purchase_timestamp"].dt.date >= default_min_date) &
        (all_df["order_purchase_timestamp"].dt.date <= default_max_date)
    ].copy()

filtered_df["order_year_month"] = filtered_df["order_purchase_timestamp"].dt.to_period("M").astype(str)

with st.sidebar:
    st.info(f"**Total pesanan:** {filtered_df['order_id'].nunique():,}")
    st.info(f"**Total pelanggan:** {filtered_df['customer_unique_id'].nunique():,}")
    st.info(f"**Total revenue:** R$ {filtered_df['revenue'].sum():,.0f}")

st.markdown("""
<div class="hero-box">
    <div class="hero-title">Dashboard Analisis E-Commerce</div>
    <div class="hero-subtitle">
        Ringkasan performa transaksi, pelanggan, kategori produk, wilayah, dan segmentasi RFM pada periode 2017–2018.
    </div>
    <span class="hero-badge">Dataset E-Commerce</span>
    <span class="hero-badge">Periode 2017–2018</span>
    <span class="hero-badge">Interactive Dashboard</span>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Total Pesanan</div>
        <div class="metric-value">{filtered_df['order_id'].nunique():,}</div>
        <div class="metric-note">Jumlah order unik dalam periode terpilih</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Total Pelanggan</div>
        <div class="metric-value">{filtered_df['customer_unique_id'].nunique():,}</div>
        <div class="metric-note">Pelanggan unik yang melakukan transaksi</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    total_revenue = filtered_df["revenue"].sum()
    revenue_display = f"R$ {total_revenue/1e6:.2f}M" if total_revenue >= 1e6 else f"R$ {total_revenue:,.0f}"
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Total Revenue</div>
        <div class="metric-value">{revenue_display}</div>
        <div class="metric-note">Akumulasi price + freight value</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    avg_order_revenue = filtered_df.groupby("order_id")["revenue"].sum().mean() if not filtered_df.empty else 0
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Avg Revenue / Order</div>
        <div class="metric-value">R$ {avg_order_revenue:.2f}</div>
        <div class="metric-note">Rata-rata nilai transaksi per order</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "Tren Bulanan",
    "Kategori Produk",
    "Distribusi Wilayah",
    "RFM Analysis"
])

with tab1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("Bagaimana tren penjualan bulanan selama periode 2017–2018?")
    st.markdown(
        '<div class="section-note">Pesanan dan revenue ditampilkan secara bulanan untuk melihat pola pertumbuhan dan periode puncak transaksi pada periode analisis.</div>',
        unsafe_allow_html=True
    )

    monthly = filtered_df.groupby("order_year_month").agg(
        order_count=("order_id", "nunique"),
        total_revenue=("revenue", "sum")
    ).reset_index()

    if len(monthly) <= 1:
        st.warning("Rentang tanggal yang dipilih terlalu sempit untuk menampilkan tren bulanan. Coba pilih rentang tanggal yang mencakup lebih dari satu bulan.")
    else:
        fig, axes = plt.subplots(2, 1, figsize=(14, 9))
        fig.patch.set_facecolor(COLOR_BG)
        x = range(len(monthly))

        axes[0].set_facecolor(COLOR_BG)
        axes[0].fill_between(x, monthly["order_count"], alpha=0.25, color=COLOR_PRIMARY)
        axes[0].plot(x, monthly["order_count"], color=COLOR_PRIMARY, linewidth=2, marker="o", markersize=4)

        peak = monthly["order_count"].idxmax()
        axes[0].annotate(
            f"{monthly.loc[peak, 'order_count']:,} pesanan",
            xy=(peak, monthly.loc[peak, "order_count"]),
            xytext=(max(0, peak - 1), monthly.loc[peak, "order_count"] * 0.88),
            arrowprops=dict(arrowstyle="->", color="#1B4332"),
            fontsize=9,
            color="#1B4332"
        )

        axes[0].set_xticks(list(x))
        axes[0].set_xticklabels(monthly["order_year_month"], rotation=45, ha="right", fontsize=8)
        axes[0].set_ylabel("Jumlah Pesanan", fontsize=11)
        axes[0].set_title("Jumlah Pesanan per Bulan Periode 2017–2018", fontsize=13, color="#1B4332")
        axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda y, _: f"{int(y):,}"))
        axes[0].spines["top"].set_visible(False)
        axes[0].spines["right"].set_visible(False)
        axes[0].grid(axis="y", linestyle="--", alpha=0.5)

        axes[1].set_facecolor(COLOR_BG)
        axes[1].fill_between(x, monthly["total_revenue"], alpha=0.25, color=COLOR_GOLD)
        axes[1].plot(x, monthly["total_revenue"], color="#C9A227", linewidth=2, marker="o", markersize=4)

        peak_rev = monthly["total_revenue"].idxmax()
        axes[1].annotate(
            f"R$ {monthly.loc[peak_rev, 'total_revenue']:,.0f}",
            xy=(peak_rev, monthly.loc[peak_rev, "total_revenue"]),
            xytext=(max(0, peak_rev - 1), monthly.loc[peak_rev, "total_revenue"] * 0.88),
            arrowprops=dict(arrowstyle="->", color="#C9A227"),
            fontsize=9,
            color="#C9A227"
        )

        axes[1].set_xticks(list(x))
        axes[1].set_xticklabels(monthly["order_year_month"], rotation=45, ha="right", fontsize=8)
        axes[1].set_ylabel("Total Revenue (R$)", fontsize=11)
        axes[1].set_title("Total Revenue per Bulan Periode 2017–2018", fontsize=13, color="#1B4332")
        axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda y, _: f"R${y/1e6:.1f}M"))
        axes[1].spines["top"].set_visible(False)
        axes[1].spines["right"].set_visible(False)
        axes[1].grid(axis="y", linestyle="--", alpha=0.5)

        plt.suptitle("Tren Pesanan dan Pendapatan Bulanan Periode 2017–2018", fontsize=15, fontweight="bold", color="#1B4332")
        plt.tight_layout()
        plt.subplots_adjust(top=0.90)
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("Kategori produk apa yang memiliki jumlah penjualan dan total revenue tertinggi selama periode 2017–2018?")
    st.markdown(
        '<div class="section-note">Perbandingan kategori terlaris berdasarkan jumlah pesanan dan kategori dengan revenue tertinggi pada periode analisis.</div>',
        unsafe_allow_html=True
    )
    top_n = st.slider("Top N Kategori", min_value=5, max_value=20, value=10)
    cat_agg = filtered_df.groupby("product_category_name_english").agg(
        total_orders=("order_id", "count"),
        total_revenue=("revenue", "sum")
    ).reset_index()

    top_orders = cat_agg.sort_values("total_orders", ascending=False).head(top_n)
    top_revenue = cat_agg.sort_values("total_revenue", ascending=False).head(top_n)

    fig, axes = plt.subplots(1, 2, figsize=(20, 8))
    fig.patch.set_facecolor(COLOR_BG)

    colors_l = [COLOR_PRIMARY if i == 0 else COLOR_MUTED for i in range(len(top_orders))]
    axes[0].set_facecolor(COLOR_BG)
    bars1 = axes[0].barh(
        top_orders["product_category_name_english"][::-1],
        top_orders["total_orders"][::-1],
        color=colors_l[::-1],
        edgecolor="white"
    )

    max_left = top_orders["total_orders"].max() if not top_orders.empty else 0
    axes[0].set_xlim(0, max_left * 1.18 if max_left > 0 else 1)

    for bar in bars1:
        w = bar.get_width()
        axes[0].text(
            w + max_left * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{int(w):,}",
            va="center",
            ha="left",
            fontsize=9,
            color="#1B4332"
        )

    axes[0].set_title(f"Top {top_n} Kategori berdasarkan Jumlah Pesanan\nPeriode 2017–2018", fontsize=12, color="#1B4332", pad=10)
    axes[0].set_xlabel("Jumlah Pesanan")
    axes[0].tick_params(axis="y", labelsize=9)
    axes[0].spines["top"].set_visible(False)
    axes[0].spines["right"].set_visible(False)
    axes[0].grid(axis="x", linestyle="--", alpha=0.5)

    colors_r = [COLOR_GOLD if i == 0 else "#F4D98A" for i in range(len(top_revenue))]
    axes[1].set_facecolor(COLOR_BG)
    bars2 = axes[1].barh(
        top_revenue["product_category_name_english"][::-1],
        top_revenue["total_revenue"][::-1],
        color=colors_r[::-1],
        edgecolor="white"
    )

    max_right = top_revenue["total_revenue"].max() if not top_revenue.empty else 0
    axes[1].set_xlim(0, max_right * 1.22 if max_right > 0 else 1)

    for bar in bars2:
        w = bar.get_width()
        label = f"R${w/1e6:.1f}M" if w >= 1e6 else f"R${w/1e3:.0f}K"
        axes[1].text(
            w + max_right * 0.01,
            bar.get_y() + bar.get_height() / 2,
            label,
            va="center",
            ha="left",
            fontsize=9,
            color="#C9A227"
        )

    axes[1].set_title(f"Top {top_n} Kategori berdasarkan Total Revenue\nPeriode 2017–2018", fontsize=12, color="#1B4332", pad=10)
    axes[1].set_xlabel("Total Revenue")
    axes[1].tick_params(axis="y", labelsize=9)
    axes[1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda y, _: f"R${y/1e6:.1f}M"))
    axes[1].spines["top"].set_visible(False)
    axes[1].spines["right"].set_visible(False)
    axes[1].grid(axis="x", linestyle="--", alpha=0.5)

    plt.suptitle("Performa Kategori Produk Periode 2017–2018", fontsize=15, fontweight="bold", color="#1B4332")
    plt.tight_layout()
    plt.subplots_adjust(top=0.88, wspace=0.35)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("Bagaimana distribusi pelanggan berdasarkan wilayah selama periode 2017–2018?")
    st.markdown(
        '<div class="section-note">Distribusi pelanggan ditinjau dari state dan kota untuk mengetahui pusat konsentrasi pasar pada periode analisis.</div>',
        unsafe_allow_html=True
    )

    bystate = filtered_df.groupby("customer_state")["customer_unique_id"].nunique().sort_values(ascending=False).reset_index()
    bystate.columns = ["customer_state", "customer_count"]

    bycity = filtered_df.groupby("customer_city")["customer_unique_id"].nunique().sort_values(ascending=False).reset_index()
    bycity.columns = ["customer_city", "customer_count"]

    fig, axes = plt.subplots(1, 2, figsize=(20, 8))
    fig.patch.set_facecolor(COLOR_BG)

    top10_state = bystate.head(10)
    colors_s = [COLOR_PRIMARY if i == 0 else COLOR_MUTED for i in range(len(top10_state))]
    axes[0].set_facecolor(COLOR_BG)
    bars = axes[0].barh(
        top10_state["customer_state"][::-1],
        top10_state["customer_count"][::-1],
        color=colors_s[::-1],
        edgecolor="white"
    )

    max_state = top10_state["customer_count"].max() if not top10_state.empty else 0
    axes[0].set_xlim(0, max_state * 1.15 if max_state > 0 else 1)

    for bar in bars:
        w = bar.get_width()
        axes[0].text(
            w + max_state * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{int(w):,}",
            va="center",
            ha="left",
            fontsize=9,
            color="#1B4332"
        )

    axes[0].set_title("Top 10 State berdasarkan Jumlah Pelanggan\nPeriode 2017–2018", fontsize=12, color="#1B4332", pad=10)
    axes[0].set_xlabel("Jumlah Pelanggan")
    axes[0].tick_params(axis="y", labelsize=9)
    axes[0].spines["top"].set_visible(False)
    axes[0].spines["right"].set_visible(False)
    axes[0].grid(axis="x", linestyle="--", alpha=0.5)

    top10_city = bycity.head(10)
    colors_c = [COLOR_PRIMARY if i == 0 else COLOR_MUTED for i in range(len(top10_city))]
    axes[1].set_facecolor(COLOR_BG)
    bars2 = axes[1].barh(
        top10_city["customer_city"][::-1],
        top10_city["customer_count"][::-1],
        color=colors_c[::-1],
        edgecolor="white"
    )

    max_city = top10_city["customer_count"].max() if not top10_city.empty else 0
    axes[1].set_xlim(0, max_city * 1.18 if max_city > 0 else 1)

    for bar in bars2:
        w = bar.get_width()
        axes[1].text(
            w + max_city * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{int(w):,}",
            va="center",
            ha="left",
            fontsize=9,
            color="#1B4332"
        )

    axes[1].set_title("Top 10 Kota berdasarkan Jumlah Pelanggan\nPeriode 2017–2018", fontsize=12, color="#1B4332", pad=10)
    axes[1].set_xlabel("Jumlah Pelanggan")
    axes[1].tick_params(axis="y", labelsize=9)
    axes[1].spines["top"].set_visible(False)
    axes[1].spines["right"].set_visible(False)
    axes[1].grid(axis="x", linestyle="--", alpha=0.5)

    plt.suptitle("Distribusi Pelanggan Berdasarkan Wilayah Periode 2017–2018", fontsize=15, fontweight="bold", color="#1B4332")
    plt.tight_layout()
    plt.subplots_adjust(top=0.88, wspace=0.35)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("Siapa pelanggan dengan nilai RFM tertinggi selama periode 2017–2018 berdasarkan Recency, Frequency, dan Monetary?")
    st.markdown(
        '<div class="section-note">Segmentasi pelanggan menggunakan Recency, Frequency, dan Monetary untuk mengidentifikasi pelanggan bernilai tinggi pada periode analisis.</div>',
        unsafe_allow_html=True
    )

    snapshot_date = filtered_df["order_purchase_timestamp"].max() + pd.Timedelta(days=30)

    rfm = filtered_df.groupby("customer_unique_id").agg(
        recency=("order_purchase_timestamp", lambda x: (snapshot_date - x.max()).days),
        frequency=("order_id", "nunique"),
        monetary=("revenue", "sum")
    ).reset_index()

    rfm["r_score"] = pd.qcut(rfm["recency"], q=5, labels=[5, 4, 3, 2, 1], duplicates="drop")
    rfm["f_score"] = pd.qcut(rfm["frequency"].rank(method="first"), q=5, labels=[1, 2, 3, 4, 5], duplicates="drop")
    rfm["m_score"] = pd.qcut(rfm["monetary"], q=5, labels=[1, 2, 3, 4, 5], duplicates="drop")
    rfm["rfm_score"] = rfm[["r_score", "f_score", "m_score"]].astype(int).sum(axis=1)

    def segment(score):
        if score >= 13:
            return "Champions"
        elif score >= 10:
            return "Loyal Customers"
        elif score >= 7:
            return "Potential Loyalists"
        elif score >= 4:
            return "At Risk"
        return "Lost"

    rfm["segment"] = rfm["rfm_score"].apply(segment)

    seg_counts = rfm["segment"].value_counts().reset_index()
    seg_counts.columns = ["segment", "count"]

    segment_order = ["Potential Loyalists", "Loyal Customers", "At Risk", "Champions", "Lost"]
    seg_counts["segment"] = pd.Categorical(seg_counts["segment"], categories=segment_order, ordered=True)
    seg_counts = seg_counts.sort_values("segment")

    seg_colors = {
        "Champions": "#1B4332",
        "Loyal Customers": "#40916C",
        "Potential Loyalists": "#74C69D",
        "At Risk": "#E9C46A",
        "Lost": "#E76F51"
    }

    col_rfm_1, col_rfm_2 = st.columns(2)

    with col_rfm_1:
        fig, ax = plt.subplots(figsize=(8, 5.5))
        fig.patch.set_facecolor(COLOR_BG)
        ax.set_facecolor(COLOR_BG)

        bars = ax.bar(
            seg_counts["segment"],
            seg_counts["count"],
            color=[seg_colors.get(s, COLOR_PRIMARY) for s in seg_counts["segment"]],
            edgecolor="white",
            width=0.6
        )

        max_seg = seg_counts["count"].max() if not seg_counts.empty else 0
        ax.set_ylim(0, max_seg * 1.15 if max_seg > 0 else 1)

        for bar in bars:
            h = bar.get_height()
            pct = h / seg_counts["count"].sum() * 100
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                h + max_seg * 0.01,
                f"{int(h):,}\n({pct:.1f}%)",
                ha="center",
                fontsize=9,
                color="#1B4332"
            )

        ax.set_title("Segmentasi Pelanggan berdasarkan RFM Score\nPeriode 2017–2018", fontsize=13, color="#1B4332", pad=10)
        ax.set_xlabel("Segmen")
        ax.set_ylabel("Jumlah Pelanggan")
        ax.tick_params(axis="x", rotation=12, labelsize=9)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="y", linestyle="--", alpha=0.5)

        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    with col_rfm_2:
        st.markdown('<div class="table-card">', unsafe_allow_html=True)
        st.markdown("### Statistik per Segmen")
        seg_stats = rfm.groupby("segment")[["recency", "frequency", "monetary"]].mean().round(2)
        seg_stats = seg_stats.reindex(["At Risk", "Champions", "Lost", "Loyal Customers", "Potential Loyalists"])
        seg_stats.columns = ["Avg Recency (hari)", "Avg Frequency", "Avg Monetary (R$)"]
        st.dataframe(seg_stats, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="table-card">', unsafe_allow_html=True)
        st.markdown("### Top 5 Champions")
        top_champ = rfm[rfm["segment"] == "Champions"].sort_values("monetary", ascending=False).head(5)
        if top_champ.empty:
            st.info("Tidak ada pelanggan pada segmen Champions untuk rentang tanggal yang dipilih.")
        else:
            if len(top_champ) < 5:
                st.caption(f"Hanya tersedia {len(top_champ)} pelanggan Champions pada rentang tanggal ini.")
            st.dataframe(
                top_champ[["customer_unique_id", "recency", "frequency", "monetary"]].reset_index(drop=True),
                use_container_width=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)
st.caption("Dashboard Proyek Fundamental Analisis Data — Seni Yanti | Dataset: E-Commerce")