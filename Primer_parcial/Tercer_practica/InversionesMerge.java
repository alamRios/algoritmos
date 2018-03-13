package inversionesmerge;
 
class InversionesMerge
{
     
    /* Ordena la matriz de Entrada y devuelve la cantidad de inversiones */
    static int mergeSort(int arr[], int array_size)
    {
        int temp[] = new int[array_size];
        return _mergeSort(arr, temp, 0, array_size - 1);
    }
      
    /* Auxiliar que ordena la matriz y regresa la cantidad */
    static int _mergeSort(int arr[], int temp[], int left, int right)
    {
      int mid, inv_count = 0;
      if (right > left)
      {
        /* divide en 2 el arreglo y llama al contador de inversiones */
        mid = (right + left)/2;
      
        /* el contador de inversiones sera la suma de las inversiones en ambas partes y el numero de inversiones en la union */
        inv_count  = _mergeSort(arr, temp, left, mid);
        inv_count += _mergeSort(arr, temp, mid+1, right);
      
        /*juntar ambas partes*/
        inv_count += merge(arr, temp, left, mid+1, right);
      }
      return inv_count;
    }
      
    /* junta ambas partes y devuelve el conteo de inversiones*/
    static int merge(int arr[], int temp[], int left, int mid, int right)
    {
      int i, j, k;
      int inv_count = 0;
      
      i = left; /* i indice del la parte izquierda*/
      j = mid;  /* j indice del la parte derecha*/
      k = left; /* k indice resultante del la union*/
      while ((i <= mid - 1) && (j <= right))
      {
        if (arr[i] <= arr[j])
        {
          temp[k++] = arr[i++];
        }
        else
        {
          temp[k++] = arr[j++];
          inv_count = inv_count + (mid - i);
        }
      }
      
      /* copia los elementos de la izquierda*/
      while (i <= mid - 1)
        temp[k++] = arr[i++];
      
      /* copia los elementos de la derecha*/
      while (j <= right)
        temp[k++] = arr[j++];
      
      /*hace el arreglo original*/
      for (i=left; i <= right; i++)
        arr[i] = temp[i];
      
      return inv_count;
    }
 
    public static void main(String[] args) 
    {
        int arr[] = new int[]{0, 1, 2, 66, 4};
        System.out.println("La cantidad de inversiones son: " + mergeSort(arr, 5));
     
    }
}
