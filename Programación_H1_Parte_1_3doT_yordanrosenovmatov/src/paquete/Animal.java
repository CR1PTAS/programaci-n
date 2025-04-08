package paquete;

public abstract class Animal {
	protected int numeroChip;
	protected String nombre;
	protected int edad;
	protected String raza;
	protected boolean adoptado;
	
	public Animal(int numeroChip, String nombre, int edad, String raza, boolean adoptado) {
		this.numeroChip = numeroChip;
		this.nombre = nombre;
		this.edad = edad;
		this.raza = raza;
		this.adoptado = adoptado;		
	}
	
	public abstract void mostrar();
}
