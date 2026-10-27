from plt_temp import transform_to_dataframe


def test_transform_dataframe():
    times = ["2023-10-28T10:00", "2023-10-28T08:00", "2023-10-28T09:00"]
    temps = [15.0, 12.0, 13.5]

    df = transform_to_dataframe(times, temps)

    assert list(df.columns) == ['time', 'temperature_c']
    assert len(df) == 3
    assert df['time'].is_monotonic_increasing
    assert df.iloc[0]['temperature_c'] == 12.0
    assert df.iloc[1]['temperature_c'] == 13.5
    assert df.iloc[2]['temperature_c'] == 15.0