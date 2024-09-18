import os
from main import (
    dataset_import,
    data_modeling,
    calculate_mean,
    calculate_median_value_creation,
    calculate_std_value_creation,
    plot_value_creation_by_industry,
)


def test_import():
    test_file_path = os.path.join(
        os.path.dirname(__file__), "test_data", "unicorn_companies.csv"
    )
    df = dataset_import(test_file_path)
    assert df is not None, "Data import failed, the dataframe is None"
    assert not df.empty, "Data import failed, the dataframe is empty"
    print("test_import passed!")


def test_modeling():
    df_raw = dataset_import()
    df_edited = data_modeling(df_raw)
    assert df_edited is not None, "Data modeling failed, the edited dataframe is None"
    assert not df_edited.empty, "Data modeling failed, the edited dataframe is empty"
    assert (
        "value_creation" in df_edited.columns
    ), "Data modeling failed, 'value_creation' column missing"
    print("test_modeling passed!")


def test_mean():
    df_raw = dataset_import()
    df_edited = data_modeling(df_raw)
    mean_value = calculate_mean(df_edited)
    assert isinstance(
        mean_value, (int, float)
    ), "Mean calculation failed, result is not a number"
    print("test_mean passed!")


def test_median():
    df_raw = dataset_import()
    df_edited = data_modeling(df_raw)
    median_value = calculate_median_value_creation(df_edited)
    assert isinstance(
        median_value, (int, float)
    ), "Median calculation failed, result is not a number"
    print("test_median passed!")


def test_stddev():
    df_raw = dataset_import()
    df_edited = data_modeling(df_raw)
    std_value = calculate_std_value_creation(df_edited)
    assert isinstance(
        std_value, (int, float)
    ), "Standard deviation calculation failed, result is not a number"
    assert (
        std_value >= 0
    ), "Standard deviation calculation failed, result is not positive"
    print("test_stddev passed!")


def test_plot():
    df_raw = dataset_import()
    df_edited = data_modeling(df_raw)
    save_dir = r"C:/Users/chris/Downloads/IDS706/chris_moriera_valuecreation_pandas/"
    plot_value_creation_by_industry(df_edited, save_dir)
    plot_path = os.path.join(save_dir, "value_creation_boxplot.png")
    assert os.path.exists(plot_path), "Plotting failed, plot was not saved"
    print("test_plot passed!")


if __name__ == "__main__":
    test_import()
    test_modeling()
    test_mean()
    test_median()
    test_stddev()
    test_plot()
    print("All tests complete & passed!")
