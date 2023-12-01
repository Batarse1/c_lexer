from enum import IntEnum

class NT(IntEnum):
    S = 0
    Type = 1
    Values = 2
    OperationAri = 3
    OperationLogic = 4
    OperationBit = 5
    Includes = 6
    Globals = 7
    GlobalsStartTypeId = 8
    DeclarationsForm = 9
    Declarator = 10
    Function = 11
    VoidFunction = 12
    Params = 13
    ParamMulti = 14
    Expression = 15
    InitialExpression = 16
    MultpleExclamation = 17
    ExpressionPrime = 18
    Statement = 19
    StatementStartId = 20
    StatementReturn = 21
    Assignation = 22
    CallFunction = 23
    CallFunctionArg = 24
    ArgumentsMulti = 25
    While = 26
    IfElse = 27