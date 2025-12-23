import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

plt.style.use("seaborn-v0_8-whitegrid")

# Вспомогательные функции
def load_and_prepare(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)
    df["ISSUE_DATE"] = pd.to_datetime(df["ISSUE_DATE"])
    df["YEAR"] = df["ISSUE_DATE"].dt.year
    df["MONTH"] = df["ISSUE_DATE"].dt.month
    df["WEEKDAY"] = df["ISSUE_DATE"].dt.day_name()
    df["Revenue"] = df["REVENUE_AMOUNT"]

    # Безопасное разбиение FOP на элементы
    if "FOP_TYPE_CODE" in df.columns:
        df["FOP_LIST"] = (
            df["FOP_TYPE_CODE"].fillna("")
            .astype(str)
            .str.split(",")
        )
    else:
        df["FOP_LIST"] = [[]] * len(df)

    return df


def add_title_page(pdf, title: str, subtitle: str):
    fig, ax = plt.subplots(figsize=(8.5, 11))
    ax.axis("off")
    ax.text(0.5, 0.7, title, fontsize=20, ha="center", va="center", weight="bold")
    ax.text(0.5, 0.65, subtitle, fontsize=12, ha="center", va="center")
    pdf.savefig(fig)
    plt.close(fig)


def page_text_block(pdf, header: str, lines: list[str]):
    fig, ax = plt.subplots(figsize=(8.5, 11))
    ax.axis("off")
    ax.text(0.05, 0.95, header, fontsize=16, weight="bold", va="top")
    y = 0.9
    for line in lines:
        ax.text(0.05, y, line, fontsize=12, va="top")
        y -= 0.04
    pdf.savefig(fig)
    plt.close(fig)


def page_dataframe_as_table(pdf, df: pd.DataFrame, title: str, max_rows=20):
    show_df = df.head(max_rows)
    fig, ax = plt.subplots(figsize=(8.5, 11))
    ax.axis("off")
    ax.set_title(title, fontsize=14, pad=10)
    table = ax.table(
        cellText=show_df.values,
        colLabels=show_df.columns,
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.2)
    pdf.savefig(fig)
    plt.close(fig)


def page_plot(pdf, fig):
    pdf.savefig(fig)
    plt.close(fig)


#  Аналитические блоки
def describe_overall(df: pd.DataFrame):
    revenue = df["Revenue"].dropna()

    stats = {
        "Количество транзакций": f"{len(revenue):,}",
        "Средняя выручка": f"{revenue.mean():.2f} руб",
        "Медианная выручка": f"{revenue.median():.2f} руб",
        "Минимальная выручка": f"{revenue.min():.2f} руб",
        "Максимальная выручка": f"{revenue.max():.2f} руб",
        "Стандартное отклонение": f"{revenue.std():.2f} руб",
        "Квартиль Q1 (25%)": f"{revenue.quantile(0.25):.2f} руб",
        "Квартиль Q3 (75%)": f"{revenue.quantile(0.75):.2f} руб",
        "Межквартильный размах": f"{revenue.quantile(0.75) - revenue.quantile(0.25):.2f} руб",
        "Коэффициент вариации": f"{revenue.std() / revenue.mean() * 100:.1f}%",
        "Доля нулевых продаж": f"{(revenue == 0).mean() * 100:.2f}%",
    }

    df_stats = pd.DataFrame(list(stats.items()), columns=["Показатель", "Значение"])

    interpretation = [
        "Распределение выручки неоднородно: высокая дисперсия и межквартильный размах.",
        "Медиана ниже среднего — присутствуют дорогие билеты, тянущие среднее вверх.",
        "Доля нулевых продаж требует проверки: возможны возвраты или ошибки.",
        "Коэффициент вариации > 50% — высокая нестабильность, стоит сегментировать по типам перелётов.",
    ]

    return df_stats, interpretation


def airports_insights(df: pd.DataFrame, n=10):
    top_orig = df["ORIG_CITY_CODE"].value_counts().head(n)
    top_dest = df["DEST_CITY_CODE"].value_counts().head(n)

    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.barh(top_orig.index, top_orig.values, color="steelblue")
    ax1.set_title("Топ аэропортов отправления")
    ax1.set_xlabel("Количество вылетов")
    ax1.grid(alpha=0.3)

    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.barh(top_dest.index, top_dest.values, color="teal")
    ax2.set_title("Топ аэропортов назначения")
    ax2.set_xlabel("Количество прилётов")
    ax2.grid(alpha=0.3)

    lines = [
        f"Ключевые аэропорты отправления: {', '.join(top_orig.index[:5])}",
        f"Ключевые аэропорты назначения: {', '.join(top_dest.index[:5])}",
        "Вывод: небольшое число хабов даёт значительную долю объёма.",
    ]
    return fig1, fig2, lines


def seasonality_block(df: pd.DataFrame):
    monthly_cnt = df.groupby("MONTH").size()
    monthly_rev = df.groupby("MONTH")["Revenue"].sum()

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    ax[0].plot(monthly_cnt.index, monthly_cnt.values, "o-", color="darkorange")
    ax[0].set_title("Количество продаж по месяцам")
    ax[0].set_xlabel("Месяц")
    ax[0].set_ylabel("Продажи")
    ax[0].set_xticks(range(1, 13))
    ax[0].grid(alpha=0.3)

    ax[1].plot(monthly_rev.index, monthly_rev.values, "o-", color="indianred")
    ax[1].set_title("Выручка по месяцам")
    ax[1].set_xlabel("Месяц")
    ax[1].set_ylabel("Выручка")
    ax[1].set_xticks(range(1, 13))
    ax[1].grid(alpha=0.3)

    lines = [
        f"Пик продаж: месяц {monthly_cnt.idxmax()}",
        f"Минимум продаж: месяц {monthly_cnt.idxmin()}",
        f"Пик выручки: месяц {monthly_rev.idxmax()}",
        f"Минимум выручки: месяц {monthly_rev.idxmin()}",
        "Вывод: присутствует сезонность как по объёму, так и по выручке.",
    ]
    return fig, lines


def passengers_block(df: pd.DataFrame):
    pax_counts = df["PAX_TYPE"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(pax_counts.values, labels=pax_counts.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Структура типов пассажиров")

    lines = [
        f"Взрослые: {(df['PAX_TYPE']=='AD').mean()*100:.1f}%",
        f"Дети: {(df['PAX_TYPE']=='CH').mean()*100:.1f}%",
        f"Младенцы: {(df['PAX_TYPE']=='IN').mean()*100:.1f}%",
        "Вывод: основная доля — взрослые пассажиры; тарифная политика должна учитывать семейные сегменты.",
    ]
    return fig, lines


def payments_block(df: pd.DataFrame, top_n=8):
    fop = df["FOP_LIST"].explode()
    fop = fop[fop != ""]
    fop_counts = fop.value_counts().head(top_n)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(fop_counts.index, fop_counts.values, color="slateblue")
    ax.set_title("Способы оплаты (топ)")
    ax.set_xlabel("Способ оплаты")
    ax.set_ylabel("Количество")
    ax.set_xticks(range(len(fop_counts)))
    ax.set_xticklabels(fop_counts.index, rotation=30)
    ax.grid(alpha=0.3)

    lines = [
        f"Основной способ оплаты: {fop_counts.index[0]}",
        "Вывод: предпочтения клиентов концентрируются вокруг нескольких способов оплаты.",
    ]
    return fig, lines


def forecast_block(df: pd.DataFrame):
    monthly = df.groupby(["YEAR", "MONTH"]).agg({"Revenue": ["sum", "count"]}).reset_index()
    monthly.columns = ["year", "month", "revenue", "tickets"]
    monthly = monthly.sort_values(["year", "month"]).reset_index(drop=True)
    monthly["t"] = np.arange(len(monthly))

    # Линейный тренд как базовый бенчмарк
    a_t, b_t = np.polyfit(monthly["t"], monthly["tickets"], 1)
    a_r, b_r = np.polyfit(monthly["t"], monthly["revenue"], 1)

    horizon = 3
    future_t = np.arange(len(monthly), len(monthly) + horizon)
    pred_tickets = a_t * future_t + b_t
    pred_revenue = a_r * future_t + b_r

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    ax[0].plot(monthly["t"], monthly["tickets"], "o-", label="Факт", color="steelblue")
    ax[0].plot(future_t, pred_tickets, "s--", label="Прогноз", color="orange")
    ax[0].set_title("Прогноз количества билетов")
    ax[0].set_ylabel("Билеты, шт")
    ax[0].legend()
    ax[0].grid(alpha=0.3)

    ax[1].plot(monthly["t"], monthly["revenue"], "o-", label="Факт", color="teal")
    ax[1].plot(future_t, pred_revenue, "s--", label="Прогноз", color="salmon")
    ax[1].set_title("Прогноз выручки")
    ax[1].set_ylabel("Выручка")
    ax[1].legend()
    ax[1].grid(alpha=0.3)

    lines = [
        f"Рост продаж (к последнему факту): +{(pred_tickets[-1]/monthly['tickets'].iloc[-1]-1)*100:.1f}%",
        f"Рост выручки (к последнему факту): +{(pred_revenue[-1]/monthly['revenue'].iloc[-1]-1)*100:.1f}%",
    ]
    return fig, lines


#  Запуск анализа и генерация PDF
def main():
    df = load_and_prepare("s7_data_sample_rev4_50k.xlsx")

    with PdfPages("sales_report.pdf") as pdf:

        # 1) Общие описательные статистики (расширенная таблица)
        stats_df, interpretation = describe_overall(df)
        page_dataframe_as_table(pdf, stats_df, "Общая описательная статистика (Revenue)")
        page_text_block(pdf, "Интерпретация статистики", interpretation)

        # 2) Определённые аэропорты (хабы)
        fig1, fig2, lines = airports_insights(df)
        page_plot(pdf, fig1)
        page_plot(pdf, fig2)
        page_text_block(pdf, "Выводы по аэропортам", lines)

        # 3) Сезонность
        fig, lines = seasonality_block(df)
        page_plot(pdf, fig)
        page_text_block(pdf, "Выводы по сезонности", lines)

        # 4) Статус/типы пассажиров
        fig, lines = passengers_block(df)
        page_plot(pdf, fig)
        page_text_block(pdf, "Выводы по пассажирам", lines)

        # 5) Способы оплаты
        fig, lines = payments_block(df)
        page_plot(pdf, fig)
        page_text_block(pdf, "Особенности способов оплаты", lines)

        # 6) Предсказание объёмов
        fig, lines = forecast_block(df)
        page_plot(pdf, fig)
        page_text_block(pdf, "Прогноз продаж (базовый тренд)", lines)

    print("PDF-отчёт сформирован")


if __name__ == "__main__":
    main()
