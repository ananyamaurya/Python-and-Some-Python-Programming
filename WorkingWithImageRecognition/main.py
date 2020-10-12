from imageai.Prediction import ImagePrediction
import os


execution_path=os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsInceptionV3()
prediction.setModelPath(os.path.join(execution_path, './models/inception_v3_weights_tf_dim_ordering_tf_kernels.h5'))
prediction.loadModel()

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "wp4589844-inosuke-hashibira-wallpapers.jpg"), result_count=5)
for eachPrediction, eachProbability in zip(predictions,probabilities):
    print(eachPrediction, " :: ", eachProbability)
