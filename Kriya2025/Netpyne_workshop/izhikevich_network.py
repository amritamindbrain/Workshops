# from netpyne import specs, sim
from netpyne import specs, sim

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Define Izhikevich Neuron Model
IZH_Neuron = {'secs': {}}
IZH_Neuron['secs']['soma'] = {'geom': {}, 'pointps': {}}
IZH_Neuron['secs']['soma']['geom'] = {'diam': 10.0, 'L': 10.0, 'cm': 31.831}  # Soma geometry
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

## Step 2: Network of 20 Izhikevich Neurons
netParams.popParams['IZHpop'] = {'cellType': 'IZH', 'numCells': 20}

## Synaptic Mechanism
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 1.0, 'tau2': 5.0, 'e': 0}  # Excitatory synapse

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 100, 'noise': 0.5}
netParams.stimTargetParams['bkg->IZH'] = {'source': 'bkg', 'conds': {'cellType': 'IZH'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

# Connectivity rules within Izhikevich population
netParams.connParams['IZH->IZH'] = {
    'preConds': {'pop': 'IZHpop'}, 'postConds': {'pop': 'IZHpop'},
    'probability': 0.1, 'weight': 0.005, 'delay': 5, 'synMech': 'exc'}

# Simulation Configuration
simConfig = specs.SimConfig()
simConfig.duration = 1000  # Simulate 1 second
simConfig.dt = 0.025  # Internal integration timestep
simConfig.verbose = False
simConfig.recordTraces = {'V_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'v'}}
simConfig.recordStep = 1  # Save data every 1ms
simConfig.filename = 'Izhikevich_Network'
simConfig.savePickle = False

# Analysis and plotting
simConfig.analysis['plotRaster'] = {'saveFig': True}  # Raster plot
simConfig.analysis['plotTraces'] = {'include': [1], 'saveFig': True}  # Voltage traces
simConfig.analysis['plot2Dnet'] = {'saveFig': True}  # 2D network visualization

# Run Simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)


