package paquete;

public class Gato extends Animal {
	private boolean testLeucemia;
	
	public Gato(int numeroChip, String nombre, int edad, String raza, boolean adoptado, boolean testLeucemia) {
	super(numeroChip, nombre, edad, raza, adoptado);
	this.testLeucemia = testLeucemia;
	}
	
	public void mostrar() {
		System.out.println("--Datos del Gato--");
		System.out.println("Número de chip: " + numeroChip);
		System.out.println("Nombre: " + nombre);
		System.out.println("Edad: " + edad);
		System.out.println("Raza: " + raza);
		System.out.println("Adoptado: " + (adoptado? "Sí" : "No"));
		System.out.println("Test de Leucemia: " + (testLeucemia? "Positivo" : "Negativo"));
	}
}
