using System;

namespace BubbleSort {
   class BubbleSort {
      static void Main(string[] args) {
         int[] arrayToSort = { 78, 55, 45, 98, 13 };
         int temp;
         for (int j = 0; j <= arrayToSort.Length - 2; j++) {
            for (int i = 0; i <= arrayToSort.Length - 2; i++) {
               if (arrayToSort[i] > arrayToSort[i + 1]) {
                  /* Sort element using temp variable */
                  temp= arrayToSortarrayToSort[i + 1];
                  arrayToSort[i + 1] = arrayToSort[i];
                  arrayToSort[i] = temp;
               }
            }
         }
         /* Show Sorted Array */
         Console.WriteLine("Sorted:");
         foreach (int p in arrayToSort)
            Console.Write(p + " ");
         Console.Read();
      }
   }
}
