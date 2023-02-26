from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str

class DataValidation:
    pass

class DataTransformtion:
    pass

class ModelTrainer:
    pass

class ModelEvaluation:
    pass

class ModelPusher:
    pass