using System;

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

public class LinkedList
{
	Node head; // Head of list

	public void push(int new_data)
	{
		Node new_node = new Node(new_data);

		new_node.next = head;

		head = new_node;
	}

	// Checks whether the value x is present in linked list
	public bool search(Node head, int x)
	{
		Node current = head; // Initialize current
		while (current != null)
		{
			if (current.data == x)
				return true; // data found
			current = current.next;
		}
		return false; // data not found
	}

	public static void Main(String []args)
	{
		LinkedList llist = new LinkedList();

		llist.push(10);
		llist.push(30);
		llist.push(11);
		llist.push(21);
		llist.push(14);

		if (llist.search(llist.head, 21))
			Console.WriteLine("Yes");
		else
			Console.WriteLine("No");
	}
}
