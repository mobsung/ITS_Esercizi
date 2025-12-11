package arcaDiNoe;

public abstract class AnimaleTerrestre implements Animale {
	
private final String categoria = "animale terrestre";
	
	public String categoria() {
		return categoria;
	}

	@Override
	public String toString() {
		return "categoria=" + categoria;
	}
}
