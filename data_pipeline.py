import pandas as pd
import xml.etree.ElementTree as ETree
import glob

dfs = []
index = 0

# Import data

emission_files = []
full_files = []

for file in glob.glob(r'/sample_input/*emissions.xml'):
    emission_files.append(file)
    #emission_files.sort()

for file in glob.glob(r'/sample_input/*full.xml'):
    full_files.append(file)
    #full_files.sort()

all_files = zip(emission_files,full_files)

# Create emissions dataframe

for dataset_emissions, dataset_full in all_files:
    prstree_emissions = ETree.parse(dataset_emissions)
    prstree_full = ETree.parse(dataset_full)
    root_emissions = prstree_emissions.getroot()
    root_full = prstree_full.getroot()
    index += 1

    time_lst = []
    vehicle_id_lst = []
    eclass_lst = []
    co2_lst = []
    co_lst = []
    hc_lst = []
    nox_lst = []
    pmx_lst = []
    fuel_lst = []
    electricity_lst = []
    noise_lst = []
    pos_lst = []
    speed_lst = []
    x_lst = []
    y_lst = []
    angle_lst = []

    for timestep in root_emissions.iter('timestep'):
        time = timestep.attrib.get('time')
        for vehicle in timestep.iter('vehicle'):
            vehicle_id = vehicle.attrib.get('id')
            eclass= vehicle.attrib.get('eclass')
            co2 = vehicle.attrib.get('CO2')
            co = vehicle.attrib.get('CO')
            hc = vehicle.attrib.get('HC')
            nox = vehicle.attrib.get('NOx')
            pmx = vehicle.attrib.get('PMx')
            fuel = vehicle.attrib.get('fuel')
            electricity = vehicle.attrib.get('electricity')
            noise = vehicle.attrib.get('noise')
            pos = vehicle.attrib.get('pos')
            speed = vehicle.attrib.get('speed')
            x = vehicle.attrib.get('x')
            y = vehicle.attrib.get('y')
            angle = vehicle.attrib.get('angle')

            time_lst.append(time)
            vehicle_id_lst.append(vehicle_id)
            eclass_lst.append(eclass)
            co2_lst.append(co2)
            co_lst.append(co2)
            hc_lst.append(hc)
            nox_lst.append(nox)
            pmx_lst.append(pmx)
            fuel_lst.append(fuel)
            electricity_lst.append(electricity)
            noise_lst.append(noise)
            pos_lst.append(pos)
            speed_lst.append(speed)
            x_lst.append(x)
            y_lst.append(y)
            angle_lst.append(angle)

    dictionary_emissions = {'time': time_lst, 'vehicle_id': vehicle_id_lst, 'eclass': eclass_lst, 'co2': co2_lst, 'co': co_lst, 'hc': hc_lst, 'nox': nox_lst, 'pmx': pmx_lst, 'fuel': fuel_lst, 'electricity':electricity_lst, 'noise': noise_lst, 'pos': pos_lst, 'speed': speed_lst, 'x': x_lst, 'y': y_lst, 'angle': angle_lst}

    df_emissions = pd.DataFrame(data=dictionary_emissions)

    # Create tl dataframe

    time_lst_tl = []
    tl_id_lst = []
    tl_state_lst = []

    for timestep in root_full.iter('data'):
        time = timestep.attrib.get('timestep')
        for tls in timestep.iter('tls'):
            for trafficlight in tls.iter('trafficlight'):
                tl_id = trafficlight.attrib.get('id')
                tl_state = trafficlight.attrib.get('state')
        time_lst_tl.append(time)
        tl_id_lst.append(tl_id)
        tl_state_lst.append(tl_state)

    dictionary_tl = {'time': time_lst_tl, 'tl_id': tl_id_lst, 'tl_state': tl_state_lst}

    df_tl = pd.DataFrame(data=dictionary_tl)

    result = pd.merge(df_emissions,df_tl, on=['time'])
    result['tl_state'] = result['tl_state'].str.replace('y', 'G')
    filename = f'dataset-{index}.csv'
    result.to_csv(filename)



