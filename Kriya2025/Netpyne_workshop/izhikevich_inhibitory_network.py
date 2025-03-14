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

## Step 3: Add Inhibitory Neurons
netParams.popParams['IZH_exc'] = {'cellType': 'IZH', 'numCells': 20}  # Excitatory population
netParams.popParams['IZH_inh'] = {'cellType': 'IZH', 'numCells': 10}  # Inhibitory population

## Synaptic Mechanism
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 1.0, 'tau2': 5.0, 'e': 10}  # Excitatory synapse
netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 2.0, 'tau2': 10.0, 'e': -70}  # Inhibitory synapse

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 100, 'noise': 0.5}
netParams.stimTargetParams['bkg->IZH_exc'] = {'source': 'bkg', 'conds': {'pop': 'IZH_exc'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

# Connectivity rules within Izhikevich population
netParams.connParams['IZH_exc->IZH_exc'] = {
    'preConds': {'pop': 'IZH_exc'}, 'postConds': {'pop': 'IZH_exc'},
    'probability': 0.1, 'weight': 0.005, 'delay': 5, 'synMech': 'exc'}

netParams.connParams['IZH_exc->IZH_inh'] = {
    'preConds': {'pop': 'IZH_exc'}, 'postConds': {'pop': 'IZH_inh'},
    'probability': 0.2, 'weight': 0.005, 'delay': 5, 'synMech': 'exc'}

netParams.connParams['IZH_inh->IZH_exc'] = {
    'preConds': {'pop': 'IZH_inh'}, 'postConds': {'pop': 'IZH_exc'},
    'probability': 0.3, 'weight': 0.007, 'delay': 3, 'synMech': 'inh'}

# Simulation Configuration
simConfig = specs.SimConfig()
simConfig.duration = 1000  # Simulate 1 second
simConfig.dt = 0.025  # Internal integration timestep
simConfig.verbose = False
simConfig.recordTraces = {'V_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'v'}}
simConfig.recordStep = 1  # Save data every 1ms
simConfig.filename = 'Izhikevich_Inhibitory_Network'
simConfig.savePickle = False

# Analysis and plotting
simConfig.analysis['plotRaster'] = {'saveFig': True}  # Raster plot
simConfig.analysis['plotTraces'] = {'include': [1], 'saveFig': True}  # Voltage traces
simConfig.analysis['plot2Dnet'] = {'saveFig': True}  # 2D network visualization

# Run Simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)
