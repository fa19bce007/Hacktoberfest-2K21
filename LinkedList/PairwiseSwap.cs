using System;
class LinkedList {
	Node head; // head of list

	public class Node {
		public int data;
		public Node next;
		public Node(int d)
		{
			data = d;
			next = null;
		}
	}

	void pairWiseSwap()
	{
		Node temp = head;

		while (temp != null && temp.next != null) {

			int k = temp.data;
			temp.data = temp.next.data;
			temp.next.data = k;
			temp = temp.next.next;
		}
	}

	/* Utility functions */
	public void push(int new_data)
	{
		/* 1 & 2: Allocate the Node &
				Put in the data*/
		Node new_node = new Node(new_data);

		/* 3. Make next of new Node as head */
		new_node.next = head;

		/* 4. Move the head to point to new Node */
		head = new_node;
	}

	void printList()
	{
		Node temp = head;
		while (temp != null) {
			Console.Write(temp.data + " ");
			temp = temp.next;
		}
		Console.WriteLine();
	}

	public static void Main(String[] args)
	{
		LinkedList llist = new LinkedList();

		llist.push(5);
		llist.push(4);
		llist.push(3);
		llist.push(2);
		llist.push(1);

		Console.WriteLine("Linked List before calling pairWiseSwap() ");
		llist.printList();

		llist.pairWiseSwap();

		Console.WriteLine("Linked List after calling pairWiseSwap() ");
		llist.printList();
	}
}
