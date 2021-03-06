import pytest

from utils_parameter_parsing import *

# constants for dummy config/CL arguments to perform testing on
PATH_TO_DUMMY_CONFIG = 'kari/test/resources/dummy_config.ini'
DUMMY_PARAMETERS_NO_COMMAND_LINE_ARGS = {'model_name': 'LSTM-CRF-NER',
'train_model': True,
'load_pretrained_model': False,
'dataset_folder': ['kari/test/resources/dummy_dataset'],
'output_folder': '../output', 'pretrained_model_weights': '',
'token_pretrained_embedding_filepath': 'kari/test/resources/dummy_word_embeddings/dummy_word_embeddings.txt',
'token_embedding_dimension': 200,
'optimizer': 'sgd', 'activation_function': 'relu', 'learning_rate': 0.01,
'gradient_clipping_value': 0.0, 'dropout_rate': 0.1, 'batch_size': 1,
'k_folds': 5, 'maximum_number_of_epochs': 10, 'max_seq_len': 50, 'debug': False,
'freeze_token_embeddings': True}
DUMMY_PARAMETERS_WITH_COMMAND_LINE_ARGS = {'model_name': 'LSTM-CRF-NER', 'train_model': True,
'load_pretrained_model': False,
'dataset_folder': ['kari/test/resources/dummy_dataset'],
'output_folder': '../output', 'pretrained_model_weights': '',
'token_pretrained_embedding_filepath': 'kari/test/resources/dummy_word_embeddings/dummy_word_embeddings.txt',
'token_embedding_dimension': 200,
'optimizer': 'sgd', 'activation_function': 'relu', 'learning_rate': 0.05,
'gradient_clipping_value': 5.0, 'dropout_rate': 0.1, 'batch_size': 1,
'k_folds': 5, 'maximum_number_of_epochs': 10, 'max_seq_len': 50, 'debug': False,
'freeze_token_embeddings': True}
DUMMY_COMMAND_LINE_ARGS = {'gradient_clipping_value': 5.0, 'learning_rate':0.05}

@pytest.fixture
def dummy_config():
    """ Returns an instance of a configparser object after parsing the dummy
    config file. """
    # parse the dummy config
    dummy_config = config_parser(PATH_TO_DUMMY_CONFIG)

    return dummy_config

def test_config_parser(dummy_config):
    """ Asserts the config object contains the expected values after parsing."""
    # check that we get the values we expected
    assert dummy_config['mode']['model_name'] == 'LSTM-CRF-NER'
    assert dummy_config['mode']['train_model'] == 'True'
    assert dummy_config['mode']['load_pretrained_model'] == 'False'

    assert dummy_config['data']['dataset_folder'] == 'kari/test/resources/dummy_dataset'
    assert dummy_config['data']['output_folder'] == '../output'
    assert dummy_config['data']['pretrained_model_weights'] == ''
    assert dummy_config['data']['token_pretrained_embedding_filepath'] == 'kari/test/resources/dummy_word_embeddings/dummy_word_embeddings.txt'

    assert dummy_config['training']['optimizer'] == 'sgd'
    assert dummy_config['training']['activation_function'] == 'relu'
    assert dummy_config['training']['learning_rate'] == '0.01'
    assert dummy_config['training']['gradient_clipping_value'] == '0'
    assert dummy_config['training']['dropout_rate'] == '0.1'
    assert dummy_config['training']['batch_size'] == '1'
    assert dummy_config['training']['k_folds'] == '5'
    assert dummy_config['training']['maximum_number_of_epochs'] == '10'
    assert dummy_config['training']['max_seq_len'] == '50'

    assert dummy_config['advanced']['debug'] == 'False'
    assert dummy_config['advanced']['freeze_token_embeddings'] == 'True'

def test_process_parameters_no_command_line_args(dummy_config):
    """ Asserts that the parameters are of the expected value/type after a
    call to process_parameters, with NO command line arguments.
    """
    # check that we get the values we expected
    assert process_parameters(dummy_config) == DUMMY_PARAMETERS_NO_COMMAND_LINE_ARGS

def test_process_parameters_command_line_args(dummy_config):
    """ Asserts that the parameters are of the expected value/type after a
    call to process_parameters, taken into account command line arguments,
    which take precedence over config arguments.
    """
    # check that we get the values we expected, specifically, check that
    # our command line arguments have overwritten our config arguments
    assert process_parameters(dummy_config, DUMMY_COMMAND_LINE_ARGS) == DUMMY_PARAMETERS_WITH_COMMAND_LINE_ARGS
