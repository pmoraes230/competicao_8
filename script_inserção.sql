/* Inserção Perfil */
INSERT INTO profile(name) VALUES
("Administrador"), ("Vendedor"), ("Totem");

/* Inserção Usuários */
INSERT INTO user(name, email, cpf, password, profile_ID) VALUES
("Patrick Nascimento", "patrick54682366@edu.pa.senac.br", "07085474270", "pbkdf2_sha256$1000000$7QqFLY7YfQSWWkVMuXx0QZ$VbdF+fj9Ot3KuW9ZWzo+7iC/BmVhWxE4gKJv488Zo80=", 1),
("Felipe Monteiro", "felipemonteiro@email.com", "54785474270", "$2a$12$x49W2XFqzVerWk3xuw6zHuVgM2scabeqNMiQpWD/5/Lz4J7PRpl1a", 1),
("Gabriel Nahun", "gabnahum@email.com", "54785474110", "$2a$12$UOP4LRJsTNevHauZSKghoOCBrUoE3aRluhHJerpw3J0ughEDu2sUa", 2),
("Maria Eduarda", "mariasemsaude@email.com", "54768241070", "$2a$12$fQaqSvaC.pQponEDfUKjiu8AvZrQatu96b6b53OU3N8hiu7A93/JW", 2),
("Mirela Ferraz", "mihferraz@email.com", "54898756310", "$2a$12$712kb7XB1z0m48JwXUYzHOSOJnedC23X8IbPX2jnyVY5c03.GpMU6", 3);

SELECT * FROM user;

/* Inserção Evento */
INSERT INTO event(event_name, limit_peaple, date_event, hour_event, description, user_ID) VALUE
("O grande show", 5000, "2025-09-20", "20:00:00", "O grande show no senac music hall com a cantora Liza", 1);

SELECT * FROM event;

/* Inserção Setor */
INSERT INTO sector(name, limit_ticket, price, event_ID) VALUES
("Público geral", 4500, 20.00, 1), ("Convidados Vips", 50, 100.00, 1), ("Imprensa credenciada", 450, 00.00, 1);

SELECT * FROM sector;

/* Inserção clientes */
INSERT INTO client(name, email, cpf) VALUES
("Pamela Nascimento", "pamelanascimento@email.com", "54587942040"),
("Patricia Moraes", "patricia@email.com", "54798752012"),
("Nielson Nascimento", "nielsonchaves@email.com", "58265998740"),
("Francisco Moraes", "franciscogato@email.com", "54896332171"),
("Augusto", "augustocompetidor@email.com", "58269785371");

SELECT * FROM client;

/* Inserção ingressos */
INSERT INTO ticket(client, event, sector_ID, id_ticket, date_issue) VALUES
(1, 1, 2, "GGSDF934HF", "2025-08-20 17:17:00"),
(1, 1, 3, "GGSDF93GEF", "2025-07-15 10:00:00"),
(4, 1, 2, "GGSDF936DA", "2025-07-15 18:00:00"),
(2, 1, 1, "GGSDF936GB", "2025-08-10 10:00:00"),
(1, 1, 3, "GGSDF93YTE", "2025-07-14 15:25:00");

SELECT * FROM ticket;