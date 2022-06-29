from housing.entity.config_entity import DataIngestionConfig,ModelTransformationConfig ,DataValidationConfig \
    , ModelTrainingConfig, ModelEvaluationConfig, ModelPusherConfig
import os

Root_dir = os.getcwd()



class Configuration:

    def __init__(self) -> None:
        pass

    def get_data_ingestion_config(self) ->DataIngestionConfig:
        pass

    def get_data_validation_config(self) ->DataValidationConfig:
        pass

    def get_data_transformation_config(self) ->ModelTransformationConfig:
        pass

    def get_model_evaluation_config(self) ->ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) ->ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) ->ModelTrainingConfig:
        try:
            training_pipeline_config = self.config_info[training_pipeline_config_key]
            artifact_dir = os.path.join(Root_dir,
            training)
        except Exception as e:
            e
