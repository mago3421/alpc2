unsigned int encodeWord(unsigned int input)
{
   unsigned int encoded = 0x00000000;
   unsigned int mask = 0x80808080;

   // Encoding
   for (int i = 0; i < 8; i++)
   {
      encoded <<= 4;
      
      if ((mask & (input & (unsigned int) 0xFF000000)) != 0x00000000)
      {
         encoded |= 0x00000008;
      }

      if ((mask & (input & (unsigned int) 0x00FF0000)) != 0x00000000)
      {
         encoded |= 0x00000004;
      }

      if ((mask & (input & (unsigned int) 0x0000FF00)) != 0x00000000)
      {
         encoded |= 0x00000002;
      }

      if ((mask & input & ((unsigned int) 0x000000FF)) != 0x00000000)
      {
         encoded |= 0x00000001;
      }

      mask >>= 1;
   }
   
   return encoded;
}


unsigned int decodeWord(unsigned int input) 
{   
   unsigned int decoded = 0x00000000;
   unsigned int mask = 0x88888888;
   
   // Decoding
   for (int i = 0; i < 4; i++)
   {
      
      decoded <<= 8;
      
      if ((mask & input & ((unsigned int) 0xF0000000)) != 0x00000000)
      {
         decoded |= 0x00000080;
      }

      if ((mask & input & ((unsigned int) 0x0F000000)) != 0x00000000)
      {
         decoded |= 0x00000040;
      }

      if ((mask & input & ((unsigned int) 0x00F00000)) != 0x00000000)
      {
         decoded |= 0x00000020;
      }

      if ((mask & input & ((unsigned int) 0x000F0000)) != 0x00000000)
      {
         decoded |= 0x00000010;
      }
                        
      if ((mask & input & ((unsigned int) 0x0000F000)) != 0x00000000)
      {
         decoded |= 0x00000008;
      }

      if ((mask & input & ((unsigned int) 0x00000F00)) != 0x00000000)
      {
         decoded |= 0x00000004;
      }

      if ((mask & input & ((unsigned int) 0x000000F0)) != 0x00000000)
      {
         decoded |= 0x00000002;
      }

      if ((mask & input & ((unsigned int) 0x0000000F)) != 0x00000000)
      {
         decoded |= 0x00000001;
      }                  
      
      mask >>= 1;
   }
   
   return decoded;
}
