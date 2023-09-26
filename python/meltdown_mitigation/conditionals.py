def is_criticality_balanced(temperature, neutrons_emitted):
    temperature_per_neutrons = temperature * neutrons_emitted
    return bool(temperature < 800 and neutrons_emitted > 500 and temperature_per_neutrons < 500000)
    
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percent = (generated_power/theoretical_max_power)*100
    if percent >= 80:
        return 'green'
    if percent < 80 and percent >= 60:
        return 'orange'
    if percent < 60 and percent >= 30:
        return 'red'
    return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    critical = temperature * neutrons_produced_per_second
    low_threshold = threshold * 0.9
    high_threshold = threshold * 1.1
    if critical < low_threshold:
        return 'LOW'
    if low_threshold <= critical <= high_threshold:
        return 'NORMAL'
    return 'DANGER'