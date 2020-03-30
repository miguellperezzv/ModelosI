
public class Singleton {
	private int valor;
	private static Singleton s = null;
	
	
	private Singleton() {
		valor=0;
	}
	
	static public Singleton getInstancia() {
		if(s==null) {
			s=new Singleton();
			System.out.println("Instancia creada");
		}
		else {
			System.out.println("Instancia ya creada");
		}
		return s;
	}

	public int getValor() {
		return valor;
		
	}

	public void setValor(int i) {
		valor=i;
		
	}

	
}
