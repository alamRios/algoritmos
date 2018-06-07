/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package huffman2;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.PriorityQueue;

/**
 *
 * @author boozh
 */
 class Nodo implements Comparable<Nodo> {
	Character caracter;
	Float frecuencia;
	Nodo izquierda;
	Nodo derecha;
	
	Nodo(Character character, Float frecuencia) {
		this.caracter = character;
		this.frecuencia = frecuencia;
	}
    
    @Override
    public int compareTo(Nodo otroNodo) {
        return this.frecuencia.compareTo(otroNodo.frecuencia);
    }
    
    @Override
    public String toString() {
        return "[ " + caracter + " : " + frecuencia + " ]";
    }
}
public class Huffman2 {
    LinkedHashMap<Character, Float> mapaCaracter; // caracter - frecuencia
    PriorityQueue<Nodo> arbol;
    Map<Character, String> codeMap;      // caracter - codificacion
	
	Huffman2() {
		/*mapaCaracter = new LinkedHashMap<Character, Float>();
                
                /*
                try{
                    try{
                FileInputStream fin = new FileInputStream("frecuencias.txt");
                ObjectInputStream ois = new ObjectInputStream(fin);
                
                Map<String, Float> mapaCaracter = (LinkedHashMap<String, Float>)ois.readObject();
                    System.out.println("Hola");
                System.out.println(m2);
                }catch(IOException | ClassNotFoundException e){
                }
                }catch(IOException ex){
                }*/
                
                
                /*
                mapaCaracter.put('_',18.3f);
                mapaCaracter.put('e',10.2f);
                mapaCaracter.put('t',7.7f);
                mapaCaracter.put('a',6.8f);
                mapaCaracter.put('o',5.9f);
                mapaCaracter.put('i',5.8f);
                mapaCaracter.put('n',5.5f);
                mapaCaracter.put('s',5.1f);
                mapaCaracter.put('h',4.9f);
                mapaCaracter.put('r',4.8f);
                mapaCaracter.put('d',3.5f);
                mapaCaracter.put('l',3.4f);
                mapaCaracter.put('c',2.6f);
                mapaCaracter.put('u',2.4f);
                mapaCaracter.put('m',2.1f);
                mapaCaracter.put('w',1.9f);
                mapaCaracter.put('f',1.8f);
                mapaCaracter.put('g',1.7f);
                mapaCaracter.put('y',1.6f);
                mapaCaracter.put('p',1.6f);
                mapaCaracter.put('b',1.3f);
                mapaCaracter.put('v',0.9f);
                mapaCaracter.put('k',0.6f);
                mapaCaracter.put('j',0.2f);
                mapaCaracter.put('x',0.2f);
                mapaCaracter.put('q',0.1f);
                mapaCaracter.put('z',0.1f);
        */
        arbol = new PriorityQueue<>();
        codeMap = new HashMap<>();
	}
   
    public static void main(String[] args) throws IOException {
        System.out.println("Cola de prioridad");
		Huffman2 conjunto = new Huffman2();
                conjunto.mapaCaracter = leerFrecuencias("frecuencias.txt");
		Nodo arbolFinal = conjunto.construirArbol();

                conjunto.construirMapadelCodigo(arbolFinal);
        
        // Decodificar caracterees
        String str = "arena";
        System.out.println("\nPrinting encoding of text : '" + str + "'");
        for(Character c : str.toCharArray()) {
            System.out.print("[" + conjunto.codeMap.get(c) + "]");
    }
    }
    private Nodo construirArbol() {
        mapaCaracter.entrySet().stream().forEach((entry) -> {
            arbol.add(new Nodo(entry.getKey(), entry.getValue()));
        });
        System.out.println(arbol);
        //System.out.println(arbol.poll() +":"+arbol.poll());
        
        while(arbol.size() > 1) {
            Nodo nodo_1 = arbol.poll();
            Nodo nodo_2 = arbol.poll();
            Nodo newNode = new Nodo('*', nodo_1.frecuencia + nodo_2.frecuencia);
            newNode.izquierda = nodo_1;
            newNode.derecha = nodo_2;
            arbol.add(newNode);
        }
        
        // El nodo que retorna es el ultimo nodo, el nodo raiz
        Nodo nodoArbolFinal = arbol.poll();
        
        System.out.println("\n Arbol de Huffman");
        desplegarArbol(nodoArbolFinal);
        return nodoArbolFinal;
	}
    
    private void desplegarArbol(Nodo raiz) {
        if(raiz != null)
            System.out.println(raiz);
        if(raiz.izquierda != null)
            desplegarArbol(raiz.izquierda);
        if(raiz.derecha != null)
            desplegarArbol(raiz.derecha);
    }
    
    private void construirMapadelCodigo(Nodo raiz) {
        int[] arr = new int[mapaCaracter.size()];
        int top = 0;
        
        System.out.println("\nCodificacion");
        imprimirCodigo(raiz, arr, top);
    }
    
    private void imprimirCodigo(Nodo raiz, int[] arr, int top) {
        if(raiz.izquierda != null) {
            arr[top] = 0;
            imprimirCodigo(raiz.izquierda, arr, top + 1);
        }
        
        if(raiz.derecha != null) {
            arr[top] = 1;
            imprimirCodigo(raiz.derecha, arr, top + 1);
        }
        
        if(esHoja(raiz)) {
            System.out.print(raiz.caracter + " : ");
            String code = imprimirArreglo(arr, top);
            codeMap.put(raiz.caracter, code);
        }
    }
    
    private String imprimirArreglo(int[] arr, int n) {
        StringBuilder resultado = new StringBuilder();
        
        for(int i = 0; i < n; i++) {
            System.out.print(arr[i]);
            resultado.append(String.valueOf(arr[i]));
        }
        System.out.println();
        return resultado.toString();
    }
    
    private boolean esHoja(Nodo raiz) {
        return (raiz.izquierda == null) && (raiz.derecha == null);
    }
    
    private static LinkedHashMap<Character, Float> leerFrecuencias(String fileName) throws IOException {
    LinkedHashMap<Character, Float> mapaCaracter_aux = new LinkedHashMap<Character, Float>();
     
    try (BufferedReader input = new BufferedReader( new FileReader("frecuencias.txt"))) {
          String linea;
            while ((linea = input.readLine()) != null) {
                dividirLinea(linea, mapaCaracter_aux);
        }
     return mapaCaracter_aux;
    }
    }
    private static void dividirLinea(String row, Map<Character, Float> mapaCaracter_aux)
            throws IOException {
        String[] columns = row.split(",");
        mapaCaracter_aux.put(columns[0].charAt(0), Float.valueOf(columns[1]));
    }
   
    
}
