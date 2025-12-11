package arcaDiNoe;

import java.util.ArrayList;

public class Arca {
	
	private ArrayList<Animale> animali = new ArrayList<>();
	
	public void salva(Animale a) {
		animali.add(a);
	}
	
	public void coro() {
		
		String s = "";
		
		for (Animale a : animali) {
			s += a.verso() + "\n";
		}
		
		System.out.println(s);
		
	}

	@Override
	public String toString() {
		
		String s = "";
		
		for (Animale a : animali) {
			s += a.toString();
		}
		
		return s;
	}
	
}
