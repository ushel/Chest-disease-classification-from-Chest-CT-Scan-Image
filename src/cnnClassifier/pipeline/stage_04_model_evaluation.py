from src.cnnClassifier.components.model_evaluation import Evaluation
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier import logger


STAGE_NAME = 'Evaluation Stage'


class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()
            
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>> Stage {STAGE_NAME} started <<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>> Stage {STAGE_NAME} completed. <<<")
    except Exception as e:
        logger.exception(e)
        raise e