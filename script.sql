CREATE TABLE IF NOT EXISTS "Backlog" (
	"id_Backlog" INTEGER NOT NULL,
	"Nome" VARCHAR(100) NOT NULL,
	"Tipo" VARCHAR(10) NOT NULL,
	"Data_criacao" DATE NOT NULL,
	"id_Projeto" INTEGER NOT NULL,
	PRIMARY KEY("id_Backlog")
);

CREATE TABLE IF NOT EXISTS "Epico" (
	"id_Epico" INTEGER NOT NULL,
	"Nome" VARCHAR(100) NOT NULL,
	"Descricao" VARCHAR(255) NOT NULL,
	"Data_criacao" DATE NOT NULL,
	"id_Projeto" INTEGER NOT NULL,
	PRIMARY KEY("id_Epico")
);

CREATE TABLE IF NOT EXISTS "Historia_Usuario" (
	"id_Historia_Usuario" INTEGER NOT NULL,
	"Nome" VARCHAR(100) NOT NULL,
	"Acao" VARCHAR(255) NOT NULL,
	"Papel" VARCHAR(255) NOT NULL,
	"Data_criacao" DATE NOT NULL,
	"Pontos_Historia" INTEGER NOT NULL,
	"MoSCoW" CHAR(1) NOT NULL,
	"RICE_Reach" INTEGER NOT NULL,
	"RICE_Impact" DECIMAL NOT NULL,
	"RICE_Confidence" DECIMAL NOT NULL,
	"RICE_Effort" INTEGER NOT NULL,
	"Status" VARCHAR(60) NOT NULL,
	"Id_Epico" INTEGER NOT NULL,
	"Id_Backlog" INTEGER NOT NULL,
	"Id_Solicitante" INTEGER NOT NULL,
	PRIMARY KEY("id_Historia_Usuario")
);

CREATE TABLE IF NOT EXISTS "Projeto" (
	"id_Projeto" INTEGER NOT NULL,
	"Nome" VARCHAR(60) NOT NULL,
	PRIMARY KEY("id_Projeto")
);

CREATE TABLE IF NOT EXISTS "Usuario" (
	"id_Usuario" INTEGER NOT NULL,
	"Nome" VARCHAR(60) NOT NULL,
	"Email" VARCHAR(100) NOT NULL,
	"Senha" VARCHAR(60) NOT NULL,
	"Papel" VARCHAR(30) NOT NULL,
	"Data_Entrada" DATE NOT NULL,
	"Data_Saida" DATE NOT NULL,
	PRIMARY KEY("id_Usuario")
);

CREATE TABLE IF NOT EXISTS "Criterio_Aceitacao" (
	"id_CriterioAceitacao" INTEGER NOT NULL,
	"Contexto_Inicial" VARCHAR(255) NOT NULL,
	"Evento" VARCHAR(255) NOT NULL,
	"Resultado" VARCHAR(255) NOT NULL,
	"Id_HistoriaUsuario" INTEGER NOT NULL,
	PRIMARY KEY("id_CriterioAceitacao")
);

ALTER TABLE "Projeto"
ADD FOREIGN KEY("id_Projeto") REFERENCES "Backlog"("id_Projeto")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Projeto"
ADD FOREIGN KEY("id_Projeto") REFERENCES "Epico"("id_Projeto")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Backlog"
ADD FOREIGN KEY("id_Backlog") REFERENCES "Historia_Usuario"("Id_Backlog")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Epico"
ADD FOREIGN KEY("id_Epico") REFERENCES "Historia_Usuario"("Id_Epico")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Usuario"
ADD FOREIGN KEY("id_Usuario") REFERENCES "Historia_Usuario"("Id_Solicitante")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "Historia_Usuario"
ADD FOREIGN KEY("id_Historia_Usuario") REFERENCES "Criterio_Aceitacao"("Id_HistoriaUsuario")
ON UPDATE NO ACTION ON DELETE NO ACTION;