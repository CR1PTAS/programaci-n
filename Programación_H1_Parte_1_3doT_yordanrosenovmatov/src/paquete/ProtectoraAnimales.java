package paquete;

import java.util.ArrayList;
import java.util.Scanner;

public class ProtectoraAnimales {
	 private static ArrayList<Animal> animales = new ArrayList<>();
	    private static Scanner scanner = new Scanner(System.in);
	    
	    public static void main(String[]args) {
	    	String opcion;
	    	do {
	    		System.out.println("--Menú de la Protectora");
	    		System.out.println("1.Dar de alta un animal");
	    		System.out.println("2.Burcar animal por número de chip");
	    		System.out.println("3.Salir");
	    		System.out.println("Seleccionar opción:");
	    		opcion = scanner.nextLine();
	    		
	    		switch (opcion) {
	    		case "1":
	    			darDeAltaAnimal();
	    			break;
	    		case "2":
	    			buscarAnimalPorChip();
	    			break;
	    		case "3":
	    			System.out.println("Saliendo del sistema");
	    			break;
	    		default:
	    			System.out.println("Opción inválidad. Intente nuevamente");
	    		}
	    	}while(!opcion.equals (3));
	    }
	    
	    private static void darDeAltaAnimal() {
	    	System.out.println("--Alta de Animal--");
	    	System.out.println("Ingresar número de chip:");
	    	int numeroChip = scanner.nextInt();
	    	
	    	if(existeNumeroChip(numeroChip)) {
	    		System.out.println("Error: El número de chip ya está registrado.");
	    		return;
	    	}
	    	
	    	System.out.println("Ingrese el nombre del animal: ");
	    	String nombre = scanner.nextLine();
	    	scanner.nextLine();
	    	System.out.println("Ingrese la edad del animal: ");
	    	int edad = scanner.nextInt();
	    	scanner.nextLine();
	    	System.out.println("Ingrese la raza del animal: ");
	    	String raza = scanner.nextLine();
	    	System.out.println("¿Está adoptado? (s/n): ");
	    	boolean adoptado = scanner.nextLine().equalsIgnoreCase("s");
	    	
	    	System.out.print("¿Es un perro o un gato? (p/g): ");
	        char tipo = scanner.nextLine().charAt(0);

	        if (tipo == 'p' || tipo == 'P') {
	            System.out.print("Ingrese el tamaño del perro (pequeño/mediano/grande): ");
	            String tamaño = scanner.nextLine();
	            animales.add(new Perro(numeroChip, nombre, edad, raza, adoptado, tamaño));
	            System.out.println("Perro registrado correctamente.");
	        } else if (tipo == 'g' || tipo == 'G') {
	            System.out.print("¿El gato tiene test de leucemia positivo? (s/n): ");
	            boolean testLeucemia = scanner.nextLine().equalsIgnoreCase("s");
	            animales.add(new Gato(numeroChip, nombre, edad, raza, adoptado, testLeucemia));
	            System.out.println("Gato registrado correctamente.");
	        } else {
	            System.out.println("Tipo de animal inválido.");
	        }
	    }
	    
	    private static boolean existeNumeroChip(int numeroChip) {
	        for (Animal animal : animales) {
	            if (animal.numeroChip == numeroChip) {
	                return true;
	            }
	        }
	        return false;
	    }
	    
	    private static void buscarAnimalPorChip() {
	        System.out.println("\n--- BUSCAR ANIMAL POR NÚMERO DE CHIP ---");
	        System.out.print("Ingrese el número de chip: ");
	        int numeroChip = scanner.nextInt();
	        scanner.nextLine(); 

	        boolean encontrado = false;
	        for (Animal animal : animales) {
	            if (animal.numeroChip == numeroChip) {
	                animal.mostrar();
	                encontrado = true;
	                break;
	            }
	        }

	        if (!encontrado) {
	            System.out.println("No se encontró ningún animal con ese número de chip.");
	        }
	    }
}
