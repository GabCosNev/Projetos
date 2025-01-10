def create_sequences(data, T):
    X = []
    Y = []
    # Loop para criar sequências a partir de 'data' com janela de tamanho T
    # O loop vai até 'len(data) - T' para evitar acessar índices fora do limite
    for t in range(len(data) - T):
        # Adiciona a sequência de entrada (T valores consecutivos de data)
        X.append(data[t:t + T])
        # Adiciona o valor seguinte à sequência como a saída (Y)
        Y.append(data[t + T])
    
    # N é o número de sequências geradas
    N = len(X)
    
    # Retorna X como um array NumPy de forma adequada, Y como array, e N como o número de sequências
    return np.array(X).reshape(-1, T), np.array(Y), N





    

