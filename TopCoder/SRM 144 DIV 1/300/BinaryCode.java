public class BinaryCode
{
	char[] msg;
	char[][] decoded = new char[2][50];
	String[] answer = new String[2];
	String NONE = "NONE";
	
	public String[] decode (String message)
	{
		int i, len, sum;
		char last, curr;
		
		msg = message.toCharArray();
		len = msg.length;
		answer[0] = answer[1] = null;
		
		switch (last = msg[0])
		{
			case '0':
				decoded[0][0] = decoded[0][1] = '0';
				answer[1] = NONE;
				break;
			case '1':
				decoded[0][0] = decoded[1][1] = '0';
				decoded[0][1] = decoded[1][0] = '1';
				break;
			case '2':
				answer[0] = NONE;
				decoded[1][0] = decoded[1][1] = '1';
				break;
			default: // '3'
				answer[0] = answer[1] = NONE;
		}
		
		if (len == 1)
		{
			sum = decoded[0][0] - '0';
		}
		else
		{
			sum = decoded[0][0] - '0' + decoded[0][1] - '0';
			for (i = 1; i < len - 1 && answer[0] == null; i++)
			{
				curr = (char) (msg[i] - sum);
				if (curr >= '0' && curr <= '1')
				{
					decoded[0][i+1] = curr;
					sum	+= curr - decoded[0][i-1];
				}
				else
				{
					answer[0] = NONE;
				}
			}
		}
		
		if (answer[0] == null)
			if (msg[len - 1] != '0' + sum)
				answer[0] = NONE;
			else
				answer[0] = new String(decoded[0], 0, len);

		if (len == 1)
		{
			sum = decoded[1][0] - '0';
		}
		else
		{
			sum = decoded[1][0] - '0' + decoded[1][1] - '0';
			for (i = 1; i < len - 1 && answer[1] == null; i++)
			{
				curr = (char) (msg[i] - sum);
				if (curr >= '0' && curr <= '1')
				{
					decoded[1][i+1] = curr;
					sum	+= curr - decoded[1][i-1];
				}
				else
				{
					answer[1] = NONE;
				}
			}
		}
		
		if (answer[1] == null)
			if (msg[len - 1] != '0' + sum)
				answer[1] = NONE;
			else
				answer[1] = new String(decoded[1], 0, len);
				
		return answer;
	}
}