from enum import Enum


class TokenType(Enum):
    NUMBER = 'NUMBER'
    KEYWORD = 'KEYWORD'
    IDENTIFIER = 'IDENTIFIER'
    OPERATOR = 'OPERATOR'
    DELIMITER = 'DELIMITER'
    STRING = 'STRING'
    COMMENT = 'COMMENT'
