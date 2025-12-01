package Tamagotchi;

public class TestTamagotchi {
	public static void main(String[] args) {
		Tamagotchi cane = new Tamagotchi("Bau");
		
		System.out.println(cane);
		
		cane.gioca();
		
		System.out.println(cane);
	}
}
