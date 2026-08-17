algoritmo "SistemaLogsAcesso"
var
   // Vetores para armazenar os detalhes do log (simulando 4 registros)
   log_usuario: vetor [1..4] de caractere
   log_datahora: vetor [1..4] de caractere
   log_status: vetor [1..4] de caractere
   i: inteiro
inicio
   // Carga inicial de dados (Simulação dos logs gerados pelo sistema)
   log_usuario[1] <- "root_admin"
   log_datahora[1] <- "2026-08-17 08:32:11"
   log_status[1]  <- "SUCESSO"

   log_usuario[2] <- "anonimo_user"
   log_datahora[2] <- "2026-08-17 09:15:44"
   log_status[2]  <- "FALHA (Senha Incorreta)"

   log_usuario[3] <- "carlos_dev"
   log_datahora[3] <- "2026-08-17 11:02:19"
   log_status[3]  <- "SUCESSO"

   log_usuario[4] <- "marta_financeiro"
   log_datahora[4] <- "2026-08-17 14:55:01"
   log_status[4]  <- "SUCESSO"

   // Exibição do Painel de Auditoria de Logs
   escreval("=========================================================")
   escreval("       PAINEL DE AUDITORIA - LOGS DE ACESSO DO SISTEMA    ")
   escreval("=========================================================")
   escreval(" DATA / HORA          | USUÁRIO          | STATUS        ")
   escreval("---------------------------------------------------------")

   // Laço para ler os vetores e organizar as colunas na tela
   para i de 1 ate 4 faca
      escreval(" ", log_datahora[i], " | ", log_usuario[i]:16, " | ", log_status[i])
   fimpara

   escreval("=========================================================")
fimalgoritmo
