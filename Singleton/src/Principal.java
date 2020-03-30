
public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Singleton singleton = Singleton.getInstancia();
		singleton.setValor(10);
		
		Singleton singleton2 = Singleton.getInstancia();
		singleton.setValor(11);

		Singleton singleton3 = Singleton.getInstancia();
		singleton.setValor(12);
		
		
		System.out.println("Valor de singleton 1 es "+ singleton.getValor());
		System.out.println("Valor de singleton 2 es "+ singleton2.getValor());
		System.out.println("Memo singleton 1 es "+ singleton.hashCode());
		System.out.println("Memo singleton 2 es "+ singleton2.hashCode());
		System.out.println("Memo singleton 3 es "+ singleton3.hashCode());
	}

}




