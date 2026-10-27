import requests
import pandas as pd
import matplotlib.pyplot as plt
def main():
    url = "https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.62&hourly=temperature_2m&forecast_days=1"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
       
    times = data['hourly']['time'][:24]
    temps = data['hourly']['temperature_2m'][:24]
       
    df = pd.DataFrame({'time': times, 'temperature_c': temps})
    df['time'] = pd.to_datetime(df['time'])
    df = df.sort_values('time').reset_index(drop=True)
       
       
    df.to_csv('temperature_24h.csv', index=False)
       
    plt.figure(figsize=(10, 5))
    plt.plot(df['time'], df['temperature_c'], marker='o')
    plt.title('Temperature in Moscow (24h)')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('temperature_24h.png')
    plt.close()

if __name__ == '__main__':
   main()