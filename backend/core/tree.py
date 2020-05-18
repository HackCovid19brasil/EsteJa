def tree(self, request):
    if float(request["leukocytes"]) <= -0.406283:
        if float(request["platelets"]) <= -0.165682:
            if float(request["hematocrit"]) <= -1.022356:
                return "NEGATIVO"
            if float(request["hematocrit"]) > -1.022356:
                if float(request["eosinophils"]) <= -0.414114:
                    if float(request["age"]) <= 10:
                        return "NEGATIVO"
                    elif float(request["age"]) > 10:
                        if float(request["lymphocytes"]) <= -1.14863:
                            return "NEGATIVO"
                        if float(request["lymphocytes"]) > -1.14863:
                            if float(request["basophils"]) <= 0.081693:
                                if float(request["mch"]) <= 0.596348:
                                    return "POSITIVO"
                                if float(request["mch"]) > 0.596348:
                                    if float(request["platelets"]) <= -0.56766:
                                        return "POSITIVO"
                                    else:
                                        return "NEGATIVO"
                            if float(request["basophils"]) > 0.081693:
                                if float(request["platelets"]) <= -1.39674:
                                    return "NEGATIVO"
                                else:
                                    if float(request["mch"]) <= 0.230447:
                                        return "POSITIVO"
                                    else:
                                        return "NEGATIVO"
                else:
                    if float(request["leukocytes"]) <= -1.063022:
                        if float(request["mch"]) <= -0.187727:
                            return "NEGATIVO"
                        else:
                            if float(request["age"]) <= 10:
                                return "NEGATIVO"
                            else:
                                return "POSITIVO"
                    else:
                        return "NEGATIVO"
        elif float(request["platelets"]) > -0.165682:
            if float(request["leukocytes"]) <= -0.729087:
                if float(request["lymphocytes"]) <= 0.130727:
                    if float(request["age"]) <= 10:
                        return "NEGATIVO"
                    else:
                        return "POSITIVO"
                if float(request["lymphocytes"]) > 0.130727:
                    return "NEGATIVO"
            else:
                return "NEGATIVO"
    else:
        return "NEGATIVO"
