from netpyne import specs, sim

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Define a single Izhikevich Neuron Model
IZH_Neuron = {'secs': {}}
IZH_Neuron['secs']['soma'] = {'geom': {}, 'pointps': {}}
IZH_Neuron['secs']['soma']['geom'] = {'diam': 30.0, 'L': 10.0, 'cm': 31.831}  # Soma geometry
IZH_Neuron['secs']['soma']['pointps']['Izhi'] = {  # Izhikevich neuron properties
    'mod': 'Izhi2007b',
    'C': 1,
    'k': 'normal(0.7, 0.05)',
    'vr': -60,
    'vt': -40,
    'vpeak': 35,
    'a': 0.03,
    'b': -2,
    'c': -50,
    'd': 100,
    'celltype': 1}
netParams.cellParams['IZH'] = IZH_Neuron  # Add Izhikevich neuron to network

## Step 1: Single Izhikevich Neuron
netParams.popParams['SingleIZH'] = {'cellType': 'IZH', 'numCells': 1}

# Stimulation for single neuron
netParams.stimSourceParams['IClamp'] = {'type': 'IClamp', 'del': 50, 'dur': 1000, 'amp': 1}
netParams.stimTargetParams['IClamp->SingleIZH'] = {'source': 'IClamp', 'conds': {'pop': 'SingleIZH'}, 'sec': 'soma', 'loc': 0.5}

# Simulation Configuration
simConfig = specs.SimConfig()
simConfig.duration = 1000  # Simulate 1 second
simConfig.dt = 0.025  # Internal integration timestep
simConfig.verbose = False
simConfig.recordTraces = {'V_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'v'}}
simConfig.recordStep = 1  # Save data every 1ms
simConfig.filename = 'Single_Izhikevich_Neuron'
simConfig.savePickle = False

# Analysis and plotting
simConfig.analysis['plotTraces'] = {'include': [0], 'saveFig': True}  # Voltage traces
simConfig.analysis['plotRaster'] = {'saveFig': True}  # Raster plot
simConfig.analysis['plot2Dnet'] = {'saveFig': True}  # 2D visualization of neuron location

# Run Simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)
