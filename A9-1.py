import soundAnalysis as SA

outputDir = "Datasets/ClustersInstrumentos"

amountOfCoeffUse = [3, 4]
SA.descriptorPairScatterPlot(outputDir, descInput=amountOfCoeffUse)
SA.showDescriptorMapping()

SA.clusterSounds(outputDir, nCluster=3, descInput=amountOfCoeffUse)

# inputSound = 'Target\\violin\\55997\\55997_692375-lq.json'
# SA.classifySoundkNN(inputSound,
# outputDir, 3, descInput=amountOfCoeffUse)

