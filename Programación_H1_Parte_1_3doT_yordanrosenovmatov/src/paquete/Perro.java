package paquete;

public class Perro extends Animal {
	private String tamaño;
	
	public Perro(int numeroChip, String nombre, int edad, String raza, boolean adoptado, String tamaño) {
		super(numeroChip, nombre, edad, raza, adoptado);
		this.tamaño = tamaño;
	}
		public void mostrar() {
	        System.out.println("-- Datos del Perro --");
	        System.out.println("Número de chip: " + numeroChip);
	        System.out.println("Nombre: " + nombre);
	        System.out.println("Edad: " + edad);
	        System.out.println("Raza: " + raza);
	        System.out.println("Adoptado: " + (adoptado ? "Sí" : "No"));
	        System.out.println("Tamaño: " + tamaño);
	}
}
