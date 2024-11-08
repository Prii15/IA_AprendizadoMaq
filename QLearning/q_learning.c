/////////////////////////////
// Q-LEARNING (Grid World)
// Autor: Danilo H. Perico
/////////////////////////////

// para cout, endl
#include <iostream>
// para usar o rand()
#include <stdlib.h>
// para sleep()
#include <unistd.h>
 

////////////////////////////////
// DEFINIÇÕES
////////////////////////////////

//namespace std para cout, endl, string
using namespace std;

// taxa de aprendizado = 20%
#define Alpha 0.2 
// fator de desconto = 90%    
#define Gamma 0.9
// porcentagem de exploração = 20%     
#define Epsilon 0.2   

// quantidade de estados, ações e experimentos
// 4 ações (cima, baixo, esquerda, direita)
#define A 4
// 3 colunas livres e 2 paredes
#define COL 5
// 3 linhas livre e duas paredes
#define LIN 5
// define quantide de estados S
#define S COL*LIN
// define quantidade de episódios
#define EPISODIOS 50

// define a representação no mapa/mundo
#define LIVRE 0
#define OBSTACULO 1
#define SAIDA 2


/////////////////////////////////
//  DECLARAÇÕES GLOBAIS
/////////////////////////////////

// matriz Q: valor estado-ação;
float Q[S][A];
// posicao na grade (x, y)
int x, y;
// auxiliar de recompensa
int rew;

// Mundo de grades:
// livre = 0
// obstaculo = 1
// saida = 2
int mapa[LIN][COL] = 
  {1, 1, 1, 2, 1,
   1, 0, 0, 0, 1,
   1, 0, 1, 1, 1,
   1, 0, 0, 0, 1,
   1, 1, 1, 1, 1 };

/////////////////////////////////
// FUNÇÕES
/////////////////////////////////

// inicializa função Q com numeros aleatorios 
// entre 0 e 1
void InitQ(float Q[S][A]) 
{
  int s,a;
  for (s=0; s<S; s++){
    for (a=0; a<A; a++) 
      // numeros aleatorios entre 0 e 1
      Q[s][a]= rand() / float(RAND_MAX);
  }
}

// inicio aleatorio do agente no mapa / mundo
void inicioAleatorio()
{
  do{
    y = rand() % LIN;
    x = rand() % COL;
  }while ((mapa[y][x] == OBSTACULO) || (mapa[y][x] == SAIDA)); 
  // while para testar se o agente não está começando  
  // na saída ou no obstáculo
}

// a partir de x e y cria o estado s
int estado(int x,int y)
{
  int s = 0;
  int i,j;
  int c = 0;  
  for (j=0;j<LIN;j++)
    for (i=0;i<COL;i++) 
    {
      if ((x==i) && (y==j)) 
        s = c;    
      c++;
    }                   
  return(s);
}

// seleciona uma acao: estratégia e-greedy
// dados Q e s
int selecionaAcao(float Q[S][A], int s)
{
  int i;
  int acao;
  int a_qmax; 
  a_qmax = 0; 
  // encontra a ação com Q maximo, dado o estado s
  for (i=1;i<A;i++){
    if (Q[s][i] > Q[s][a_qmax])
      a_qmax = i;
  }
  acao = a_qmax;        
 
  // e-greedy: 
  // escolhe a ação com Q maximo ou escolhe ação aleatória
  // gera número aleatório
  float e = rand() % 1000 / 1000;
  if (e < Epsilon)
    // gera ação aleatória 
    acao = rand() % A;
  return (acao);
}

// obtém o próximo estado e verifica se colisões
// utiliza rew para armazenar colisão
int proximoEstado(int a)
{
  rew = 0;
   // ações a={0,1,2,3}
   // {para baixo, para direita, para cima, para esquerda}
  switch(a){
    // para baixo
    case 0: 
      if(mapa[y+1][x] != 1)           
        y += 1 ;
      else
        rew = 1;
        break;
      // para direita
      case 1: 
        if(mapa[y][x+1] != 1) 
          x += 1 ;
        else
          rew = 1;
        break;
      // para cima
      case 2: 
        if(mapa[y-1][x] != 1)
          y -= 1;
        else
          rew = 1;
        break;
      // para esquerda
      case 3: 
        if(mapa[y][x-1] != 1)
          x -= 1;
        else
          rew = 1;
        break;
    }
  return(estado(x,y));
}

// retorna a recompensa
int recompensa()
{ 
  // 100 caso encontre o objetivo
  // -5 quando colidir
  // -1 para cada ação que não resultar no objetivo
  if(mapa[y][x] == SAIDA)
      return(100);
  else{
    if (rew == 1)
      return(-5);
    else
      return(-1); 
  }    
}

// função para atualizar o valor de Q
void atualizaQ(int s,int a, int r, float Q[S][A], int next_s, int next_a)
{
  Q[s][a]=Q[s][a]+Alpha*(r+Gamma*Q[next_s][next_a]-Q[s][a]);        
}
         
// desenha a politica de ações 
// simula o mundo
void desenhaMapaPolitica(int espaco[S], int episodio)
{
  int linha, coluna;   
  cout << endl;
  cout << endl;
  cout << endl;
  cout << " ===== Q-LEARNING ===== " << endl;
  cout << endl;
  cout << "Episódio: " << episodio << endl;
  cout << endl;

  for (linha=0;linha<LIN;linha++){
    for (coluna=0;coluna<COL;coluna++){
      if (mapa[linha][coluna] == LIVRE){
        int esp = estado(coluna,linha);       
        switch(espaco[esp]){               
          case 0:
            cout << "v"; //seta para baixo           
            break;
          case 1: 
            cout << ">"; //seta para direita         
            break;
          case 2: 
            cout << "^"; //seta para cima          
            break;
          case 3: 
            cout << "<"; //seta para esquerda         
            break;
        }
 
      }    
      if (mapa[linha][coluna] == OBSTACULO)
        cout << "#";
      else if (mapa[linha][coluna] == SAIDA)
        cout << " ";           
    }
    cout << endl;
  }
}


////////////////////////////////
// CÓDIGO PRINCIPAL (main)
////////////////////////////////

int main()
{
  // para gerar os números aleatórios
  srand((unsigned) time(NULL));
  // ação a ser tomada
  int at;
  // estado
  int s;
  // proximo estado e proxima acao
  int s_proximo, a_proximo;
  // recompensa
  int r;
  // para contar quantidade de episodios
  int episodio; 

  // inicializa Q aleatoriamente
  InitQ(Q);

  // imprime Q inicial - somente para debug
  // linhas são estados, colunas são ações
  cout << "Tabela Q inicial" << endl;
  for (int s=0;s<S;s++){
    for (int a=0;a<A;a++) 
      cout << Q[s][a] << " ";
    cout << endl;
  }

  // repete EPISODIOS vezes 
  for (episodio = 0; episodio < EPISODIOS; episodio++) 
  {      
    // inicia o agente aleatoriamente
    inicioAleatorio();
    // pega estado inicial e localiza na grade 
    s = estado(x,y); 
    // repete até encontrar o objetivo 
    while (mapa[y][x] != SAIDA){
      // seleciona uma ação at, dados Q e s
      at = selecionaAcao(Q,s);
      // com a ação escolhida, obtém o próximo estado s 
      s_proximo = proximoEstado(at);  
      // recebe a recompensa
      r = recompensa(); 
      // seleciona próxima ação
      a_proximo = selecionaAcao(Q,s_proximo);  
      // atualiza a matriz Q           
      atualizaQ(s, at, r, Q, s_proximo, a_proximo);
      // o estado atual passa a ser igual ao próximo estado 
      s = s_proximo;          
    }  
    
    // desenha a política no terminal 
    // a cada x episodios
    int x = 5;
    int politica[S];
    if(episodio % x == 0){
      for (s=0 ; s<S ; s++){
        int a_qmax = 0;
        for (int i=1;i<A;i++){
          if (Q[s][i] > Q[s][a_qmax])
            a_qmax = i;
        }
        politica[s] = a_qmax;
      }
      // imprime na tela somente a ação que
      // maximiza Q
      desenhaMapaPolitica(politica, episodio);
      // atualiza a cada 1 segundo
      sleep(1);
    }
  }
  // imprime Q final - somente para debug
  // linhas são estados, colunas são ações
  cout << endl;
  cout << "Tabela Q final" << endl;
  for (int s=0;s<S;s++){
    for (int a=0;a<A;a++) 
      cout << Q[s][a] << " ";
    cout << endl;
  }      
}