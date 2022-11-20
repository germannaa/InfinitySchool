CREATE DATABASE loja113;
use loja113;

create table usuario(
nome_usuario varchar(50) not null,
endereco_usuario varchar(50) not null,
idade_usuario int not null,

primary key (nome_usuario)
);
