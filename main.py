__author__ = 'Rober_001'

from View import View
from MatchTimeConvertor import MatchConverter
from Weka_MatchGenerator_Local import LableGenerator
from file_feature_extraction import file_feature_extraction


def showTestModel(audioFile, matchFile, windowSize, stepSize):
    print(audioFile)
    print(matchFile)
    print(windowSize)
    print(stepSize)

    featureArray = file_feature_extraction(audioFile)
    my_matchConverter = MatchConverter(matchFile, 0)
    timesList = my_matchConverter.convert()

    my_labelGenerator = LableGenerator(timesList, len(featureArray), int(windowSize))
    labels = my_labelGenerator.generate()

    print(labels)

    my_view.showTestModelScreen()


my_view = View(500, 500)

my_view.showPrepareScreen(showTestModel)

my_view.start()


