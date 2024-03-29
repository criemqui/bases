CREATE TABLE Categoria (
ID SERIAL PRIMARY KEY,
Nombre VARCHAR
);

CREATE TABLE Producto (
ID SERIAL PRIMARY KEY,
Nombre VARCHAR,
Marca VARCHAR,
Categoria_ID INTEGER REFERENCES Categoria_ID,
Precio_unitario INTEGER
);

CREATE TABLE Sucursal (
ID SERIAL PRIMARY KEY,
Nombre VARCHAR, 
Direccion VARCHAR
);

CREATE TABLE Stock (
    ID SERIAL PRIMARY KEY, 
    Sucursal_ID INTEGER REFERENCES Sucursal(ID) NOT NULL, 
    Producto_ID INTEGER REFERENCES Producto(ID) NOT NULL, 
    Cantidad INTEGER, 
    UNIQUE (Sucursal_ID, Producto_ID)
);


CREATE TABLE Cliente (
ID SERIAL PRIMARY KEY, 
Nombre VARCHAR, 
Telefono INTEGER
);

CREATE TABLE Orden (
ID SERIAL PRIMARY KEY, 
Cliente_ID INTEGER REFERENCES Cliente(ID), 
Sucursal_ID INTEGER REFERENCES Sucursal(ID), 
Fecha timestamp, 
Total INTEGER
);

CREATE TABLE Item (
ID SERIAL PRIMARY KEY, 
Orden_ID INTEGER REFERENCES Orden(ID), 
Producto_ID INTEGER REFERENCES Producto(ID), 
Cantidad INTEGER, 
Monto_venta INTEGER
);