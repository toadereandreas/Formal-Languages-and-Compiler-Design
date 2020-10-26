import re

reservedWords = []
separators = []
operators = []

def readFile():
    with open('Token.in.txt', 'r') as f:
        f.readline()
        for i in range(17):
            separator = f.readline().strip()
            if separator == "<space>":
                separator = " "
            separators.append(separator)
        print("Separators = " + str(separators))
        for i in range(10):
            operators.append(f.readline().strip())
        print("Operators = " + str(operators))
        for i in range(15):
            reservedWords.append(f.readline().strip())
        print("Reserver words = " + str(reservedWords))


class Scanner:

    def getStringToken(self, line, index):
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '\'':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    def isPartOfOperator(self, char):
        for op in operators:
            if char in op:
                return True
        return False

    def getOperatorToken(self, line, index):
        token = ''
        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def tokenize(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.isPartOfOperator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.getOperatorToken(line, index)
                tokens.append(token)
                token = ''  # reset token

            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.getStringToken(line, index)
                tokens.append(token)
                token = ''  # reset token

            elif line[index] in separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''  # reset token

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def isIdentifier(self, token):
        return re.match(r'^[a-z]([a-zA-Z]|[0-9]){,7}', token) is not None

    def isConstant(self, token):
        return re.match(r'^(0|[+\-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None
