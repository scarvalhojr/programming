
class Bloco
{
	public int numero;
	public int fila;
	public Bloco anterior;
	public Bloco proximo;

	public Bloco (int numero)
	{
		this.numero = numero;
		this.fila = numero;
		this.anterior = null;
		this.proximo = null;
	}
}

public class BlockWorld
{
	private static final boolean MODO_DEPURACAO = true;
	private static String tabulacao = "";

	private static int dimensao;
	private static Bloco[] bloco;
	private static Bloco[] fila;

	public static void main (String args[])
	{
		iniciar(10);
		moveOnto(9,1);
		moveOver(8,1);
		moveOver(7,1);
		moveOver(6,1);
		pileOver(8,6);
		pileOver(8,5);
		moveOver(2,1);
		moveOver(4,9);

		/*
		moveOnto(2,4);
		moveOnto(4,3);
		pileOnto(3,2);
		pileOver(5,6);
		pileOver(3,6);
		pileOnto(3,7);
		moveOnto(6,3);
		*/
	}

	/**
	 * Instancia os blocos e forma a configuração inicial das filas.
	 */
	private static void iniciar (int dim)
	{
		// Configura a dimensão
		dimensao = dim;

		if (MODO_DEPURACAO) System.out.println("METODO iniciar (" + dim + ")");

		// Cria o vetor de apontadores diretos para os blocos
		bloco = new Bloco[dimensao];

		// Cria o vetor filas de blocos
		fila = new Bloco[dimensao];

		// Instancia os blocos e configura as filas
		for (int num = 0; num < dim; num++)
		{
			bloco[num] = new Bloco(num);
			fila[num] = bloco[num];
		}

		if (MODO_DEPURACAO) mostrarFilas();
	}

	/**
	 * Retira blocos que estão empilhados em cima de um determinado bloco,
	 * movendo-os para as suas filas originais.
	 */
	private static void liberarBloco (int numbloco)
	{
		Bloco b, temp;

		if (MODO_DEPURACAO) System.out.println("METODO liberarBloco (" + numbloco + ")");

		// Obtém um ponteiro pro bloco a partir do seu número
		b = bloco[numbloco];

		// Se não existem blocos empilhados: nada a fazer
		if (b.proximo == null) return;

		// Percorre a lista de blocos empilhados,
		// movendo-os para as suas filas originais
		b = b.proximo;
		while (b != null)
		{
			if (MODO_DEPURACAO) System.out.println("  Movendo bloco " + b.numero + " para a sua fila original");

			// Move o bloco empilhado para a sua fila
			moverBloco(b, b.numero);

			// Passa para o próximo
			temp = b.proximo;
			b.proximo = null;
			b = temp;
		}

		if (MODO_DEPURACAO) mostrarFilas();
	}

	/**
	 * Move um bloco para uma determinada filha,
	 * organizando a estrutura de ponteiros.
	 */
	private static void moverBloco (int numbloco, int numfila)
	{
		moverBloco (bloco[numbloco], numfila);
	}

	/**
	 * Move um bloco para uma determinada filha,
	 * organizando a estrutura de ponteiros.
	 */
	private static void moverBloco (Bloco b, int numfila)
	{
		Bloco f;

		if (MODO_DEPURACAO) System.out.println("METODO moverBloco (" + b.numero + ", " + numfila + ")");

		// Verifica se o bloco é o primeiro da sua fila atual
		if (b.anterior == null)
		{
			// Sim: esvazia a fila
			fila[b.fila] = null;

			if (MODO_DEPURACAO) System.out.println("  A fila " + b.fila + " esta vazia: anulando ponteiro");
		}
		else
		{
			// Não: torna nulo o ponteiro do
			// bloco imediatamente anterior
			(b.anterior).proximo = null;

			if (MODO_DEPURACAO) System.out.println("  Anulando o ponteiro 'proximo' do bloco anterior (" + (b.anterior).numero + ")");
		}

		// Verifica se a fila destino está vazia
		if (fila[numfila] == null)
		{
			// Sim: o bloco será o primeiro da fila
			fila[numfila] = b;
			b.anterior = null;

			if (MODO_DEPURACAO) System.out.println("  A fila destino esta vazia ");
		}
		else
		{
			if (MODO_DEPURACAO) System.out.println("  A fila destino nao esta vazia: procurando ultimo bloco da fila");

			// A fila destino nao esta vazia: procura o último bloco da fila
			f = fila[numfila];
			while (f.proximo != null)
				f = f.proximo;

			if (MODO_DEPURACAO) System.out.println("  Ultimo bloco (" + f.numero + ") encontrado");

			// Insere o novo bloco no final da fila
			f.proximo = b;
			b.anterior = f;
		}

		// Atualiza o indicador de fila do bloco
		b.fila = numfila;
	}

	/**
	 * Move uma pilha de blocos iniciada pelo bloco b
	 * para uma determinada fila
	 */
	private static void moverPilha (int numbloco, int numfila)
	{
		Bloco b = bloco[numbloco];

		if (MODO_DEPURACAO) System.out.println("METODO moverPilha (" + numbloco + ", " + numfila + ")");

		// Move o primeiro bloco e mantém
		// a estrutura de ponteiros
		moverBloco(b, numfila);

		// Percorre os demais blocos atualizando
		// o indicador de fila
		while (b.proximo != null)
		{
			b = b.proximo;
			b.fila = numfila;
		}
	}

	private static void lerComandos ()
	{
		int comando, bloco_origem, bloco_destino;

		//System.out.println(
	}

	/**
	 * moveOnto
	 */
	private static void moveOnto (int bloco_origem, int bloco_destino)
	{
		// Retira os blocos empilhados sobre o bloco de
		// origem, movendo-os para as suas filas originais
		liberarBloco(bloco_origem);

		// Retira os blocos empilhados sobre o bloco de
		// destino, movendo-os para as suas filas originais
		liberarBloco(bloco_destino);

		// Move o bloco de origem para a fila do bloco de destino
		moverBloco(bloco_origem, bloco[bloco_destino].fila);

		if(MODO_DEPURACAO)
		{
			System.out.print("\n\nMove onto (" + bloco_origem + "," + bloco_destino + ")");
			mostrarFilas();
		}
	}

	/**
	 * moveOver
	 */
	private static void moveOver (int bloco_origem, int bloco_destino)
	{
		// Retira os blocos empilhados sobre o bloco de
		// origem, movendo-os para as suas filas originais
		liberarBloco(bloco_origem);

		// Move o bloco de origem para a fila do bloco de destino
		moverBloco(bloco_origem, bloco[bloco_destino].fila);

		if(MODO_DEPURACAO)
		{
			System.out.print("\n\nMove over (" + bloco_origem + "," + bloco_destino + ")");
			mostrarFilas();
		}
	}

	/**
	 * pileOnto
	 */
	private static void pileOnto (int bloco_origem, int bloco_destino)
	{
		// Retira os blocos empilhados sobre o bloco de
		// destino, movendo-os para as suas filas originais
		liberarBloco(bloco_destino);

		// Move a pilha iniciada pelo bloco de origem para a fila do bloco de destino
		moverPilha(bloco_origem, bloco[bloco_destino].fila);

		if(MODO_DEPURACAO)
		{
			System.out.print("\n\nPile onto (" + bloco_origem + "," + bloco_destino + ")");
			mostrarFilas();
		}
	}

	/**
	 * pileOver
	 */
	private static void pileOver (int bloco_origem, int bloco_destino)
	{
		// Move a pilha iniciada pelo bloco de origem para a fila do bloco de destino
		moverPilha(bloco_origem, bloco[bloco_destino].fila);

		if(MODO_DEPURACAO)
		{
			System.out.print("\n\nPile over (" + bloco_origem + "," + bloco_destino + ")");
			mostrarFilas();
		}
	}

	/**
	 * Exibe o estado atual das filas.
	 */
	private static void mostrarFilas ()
	{
		Bloco b;

		System.out.print("\nEstado atual do mundo:");

		// Percorre todas as filas
		for (int numfila = 0; numfila < dimensao; numfila++)
		{
			System.out.print("\n" + numfila + ":");

			// Percorre todos os blocos da fila
			b = fila[numfila];
			while (b != null)
			{
				// Imprime o número do bloco
				System.out.print(" " + b.numero);

				// Verifica se o bloco está com a numeração da fila correta
				if (b.fila != numfila) System.out.print("(" + b.fila + ")");

				// Passa para o próximo bloco
				b = b.proximo;
			}
		}
	}

}