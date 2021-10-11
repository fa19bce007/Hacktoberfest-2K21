// Recursive C# program to
// reverse a linked list
using System;
class recursion{
	
// Head of list
static Node head;

public class Node
{
public int data;
public Node next;
public Node(int d)
{
	data = d;
	next = null;
}
}

static Node reverse(Node head)
{
if (head == null ||
	head.next == null)
	return head;

// Reverse the rest list and put
// the first element at the end
Node rest = reverse(head.next);
head.next.next = head;

// Tricky step --
// see the diagram
head.next = null;

// Fix the head pointer
return rest;
}

// Function to print
// linked list
static void print()
{
Node temp = head;
while (temp != null)
{
	Console.Write(temp.data + " ");
	temp = temp.next;
}
Console.WriteLine();
}

static void push(int data)
{
Node temp = new Node(data);
temp.next = head;
head = temp;
}

// Driver code
public static void Main(String []args)
{
// Start with the
// empty list
push(20);
push(4);
push(15);
push(85);

Console.WriteLine("Given linked list");
print();
head = reverse(head);
Console.WriteLine("Reversed Linked list");
print();
}
}

// This code is contributed by gauravrajput1
