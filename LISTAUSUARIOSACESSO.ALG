algoritmo "ListaUsuariosAcesso"
var
   // Cria um vetor (lista) para guardar até 5 nomes de usuários
   usuarios: vetor [1..5] de caractere
   i: inteiro
inicio
   // Cadastro simulado dos usuários que acessaram o PC
   usuarios[1] <- "Administrador"
   usuarios[2] <- "Ana_Silva"
   usuarios[3] <- "Suporte_TI"
   usuarios[4] <- "Carlos_Dev"
   usuarios[5] <- "Usuario_Convidado"

   // Exibição do relatório de acessos
   escreval("=========================================")
   escreval("   RELATÓRIO DE ACESSOS AO COMPUTADOR    ")
   escreval("=========================================")
   escreval("Usuários que fizeram login recentemente:")
   escreval("-----------------------------------------")

   // Laço para percorrer a lista e mostrar nome por nome
   para i de 1 ate 5 faca
      escreval(" > ID: ", i, " | Usuário: ", usuarios[i])
   fimpara

   escreval("=========================================")
fimalgoritmo
