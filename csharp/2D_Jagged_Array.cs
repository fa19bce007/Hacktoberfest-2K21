using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int rows;
            Console.WriteLine("---Enter No of rows of array: ");
            rows = Convert.ToInt32(Console.ReadLine());
           
            int[][] array1 = new int[rows][];
            for (int z = 0; z < rows; z++)
            {
                Console.WriteLine("Enter no of cols in row " + (z+1) + ": ");
                int cols = Convert.ToInt32(Console.ReadLine());
                array1[z] = new int[cols];
            }

           
            for (int z = 0; z < rows; z++)
            {
                for (int x = 0; x < array1[z].Length; x++)
                {
                    Console.Write("Enter at column "+(x+1));
                    array1[z][x] = Convert.ToInt32(Console.ReadLine());
                }
            }
           
            for (int z = 0; z < rows; z++)
            {
                for (int x = 0; x < array1[z].Length; x++)
                {
                    if ((array1[z][x] % 2) == 0)
                    {
                        Console.Write("even numbers are  "+array1[z][x] + "\n");
                    }
                    else
                    {
                        Console.Write("Odd Numbers are "+array1[z][x] + " ");

                    }
                }
                Console.WriteLine();
            }

            Console.ReadKey();
        }
    }
    }

