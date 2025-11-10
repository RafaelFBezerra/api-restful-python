CREATE TABLE IF NOT EXISTS clientes (
    cliente_id SERIAL PRIMARY KEY,
    nome VARCHAR(1000) NOT NULL,
    email VARCHAR(1000) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos_favoritos(
    cliente_id INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    titulo VARCHAR(1000) NOT NULL,
    imagem VARCHAR(10000) NOT NULL,
    preco VARCHAR(100) NOT NULL,
    review VARCHAR(10000),
    
    FOREIGN KEY (cliente_id) 
    REFERENCES clientes (cliente_id) 
    ON DELETE CASCADE,
    PRIMARY KEY (cliente_id, id_produto)
)
