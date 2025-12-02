package Tamagotchi;

import Tamagotchi.Tamagotchi.Specie;

public class TestTamagotchi {
	public static void main(String[] args) {
		Tamagotchi cane = new Tamagotchi("Bau", Specie.GATTO);
		
		System.out.println(cane);
		
		cane.gioca();
		
		System.out.println(cane);
	}
}
